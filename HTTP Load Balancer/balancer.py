# lb.py
import socket
import threading
import time
import requests
import asyncio

class RoundRobinLoadBalancer:
    def __init__(self, backend_servers):
        self.backend_servers = backend_servers
        self.current_index = 0
        self.lock = threading.Lock()

    def get_next_server(self):
        with self.lock:
            server = self.backend_servers[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.backend_servers)
        return server

    async def health_check(self, server):
        health_check_url = f"http://{server[0]}:{server[1]}/health"
        try:
            response = await asyncio.to_thread(requests.get, health_check_url)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

    async def start_health_check_task(self, interval_seconds):
        while True:
            for server in self.backend_servers.copy():
                if not await self.health_check(server):
                    print(f"Server {server} failed health check. Removing from rotation.")
                    with self.lock:
                        self.backend_servers.remove(server)
            await asyncio.sleep(interval_seconds)

async def handle_client(client_socket, load_balancer):
    request = await asyncio.to_thread(client_socket.recv, 1024)
    print(f"Received request from {client_socket.getpeername()}\n{request.decode()}")

    # Forward request to backend server using Round Robin
    backend_server = load_balancer.get_next_server()
    backend_response = await asyncio.to_thread(forward_request_to_backend, request, backend_server)

    # Send backend response to client
    await asyncio.to_thread(client_socket.sendall, backend_response)
    client_socket.close()

def forward_request_to_backend(request, backend_server):
    # Implement forwarding logic to backend server
    # ...

    # For testing purposes, simulate a backend response
    return b"HTTP/1.1 200 OK\n\nHello From Backend Server"

async def start_load_balancer(port, backend_servers):
    lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lb_socket.bind(("0.0.0.0", port))
    lb_socket.listen(5)

    print(f"Load balancer listening on port {port}...")

    load_balancer = RoundRobinLoadBalancer(backend_servers)

    # Start health check task in the background
    health_check_task = asyncio.create_task(load_balancer.start_health_check_task(10))

    while True:
        client_socket, addr = lb_socket.accept()
        asyncio.create_task(handle_client(client_socket, load_balancer))

if __name__ == "__main__":
    backend_servers = [
        ("localhost", 8080),
        ("localhost", 8081),
        ("localhost", 8082),
        # Add more servers as needed
    ]
    
    # Create and run the event loop
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(start_load_balancer(80, backend_servers))
        loop.run_forever()
    finally:
        loop.close()
