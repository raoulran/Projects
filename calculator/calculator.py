import tkinter as tk
from tkinter import ttk
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Radotlator")
        self.master.geometry("600x400")
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.current_calculator = None
        self.create_widgets()

    def create_widgets(self):
        self.create_calculator_frame()

    def create_calculator_frame(self):
        self.calculator_frame = tk.Frame(self.master, bg="#2C2F33", bd=5)
        self.calculator_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        entry_frame = tk.Frame(self.calculator_frame, bg="#2C2F33", bd=5)
        entry_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        self.entry = tk.Entry(entry_frame, font=("Arial", 24), textvariable=self.result_var, justify="right", bg="#121212", fg="white")
        self.entry.grid(row=0, column=0, sticky="nsew")
        entry_frame.grid_columnconfigure(0, weight=1)

        button_frame = tk.Frame(self.calculator_frame, bg="#2C2F33", bd=5)
        button_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("DEL", 5, 1)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 18),
                command=lambda t=text: self.on_button_click(t),
                bg="#2C2F33", fg="white"
            )
            btn.grid(row=row, column=col, sticky="nsew")

        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
            button_frame.grid_columnconfigure(i, weight=1)

        scientific_buttons = [
            ("sin", 5, 2), ("cos", 5, 3), ("tan", 5, 4), ("deg", 6, 2),
            ("rad", 6, 3), ("log", 6, 4), ("ln", 7, 2), ("e", 7, 3),
            ("π", 7, 4), ("^", 8, 2), ("(", 8, 3), (")", 8, 4), ("sqrt", 9, 2),
            ("!", 9, 3), ("±", 9, 4)
        ]

        for (text, row, col) in scientific_buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 12),
                command=lambda t=text: self.on_button_click(t),
                bg="#2C2F33", fg="white"
            )
            btn.grid(row=row, column=col, sticky="nsew")

        button_frame.grid_columnconfigure(4, weight=1)

    def on_button_click(self, value):
        if value == "=":
            self.calculate_result()
        elif value == "C":
            self.result_var.set("0")
        elif value == "DEL":
            current_value = self.result_var.get()
            if len(current_value) > 1:
                self.result_var.set(current_value[:-1])
            else:
                self.result_var.set("0")
        elif value == "±":
            self.result_var.set(str(-float(self.result_var.get())))
        else:
            current_value = self.result_var.get()
            if current_value == "0":
                self.result_var.set(value)
            else:
                self.result_var.set(current_value + value)

        # Set focus to the Entry widget after button click
        self.entry.focus_set()

    def calculate_result(self):
        try:
            expression = self.result_var.get().replace("^", "**").replace("√", "sqrt").replace("π", str(math.pi))
            result = eval(expression)
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

