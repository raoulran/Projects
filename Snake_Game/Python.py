from tkinter import*
import random
import tkinter

GAME_WIDTH= 700
GAME_HEIGHT= 700
SPEED= 100
SPACE_SIZE= 20
BODY_PART= 3
SNAKE_COLOR="Green"
FOOD_COLOR="Red"
BACKGROUND_COLOR="Black"  

class Snake:
    
    def __init__(self):
        self.body_size=BODY_PART
        self.coordinate=[]
        self.square=[]
        for i in range(0,BODY_PART):
            self.coordinate.append([0,0])
        for x , y in self.coordinate:
            square=canvas.create_rectangle(x,y, x+SPACE_SIZE , y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.square.append(square)

class Food:
    def __init__(self) :
        
        x=random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y=random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        
        self.coordinate=[x,y]
        canvas.create_oval(x, y, x +SPACE_SIZE,  y +SPACE_SIZE, fill=FOOD_COLOR, tags= "food")

def Next_turn(snake , food):
    
    X,Y=snake.coordinate[0]
    
    if direction=="up":
        Y -=SPACE_SIZE
        
    elif direction=="down":
        Y += SPACE_SIZE
        
    elif direction=="left":
        X -= SPACE_SIZE
        
    elif direction=="right":
        X += SPACE_SIZE
        
    snake.coordinate.insert(0,(X,Y))
    
    square= canvas.create_rectangle(X ,Y , X + SPACE_SIZE , Y + SPACE_SIZE , fill=SNAKE_COLOR)
    
    snake.square.insert(0 , square)
    
    if X == food.coordinate[0] and Y == food.coordinate[1]:
        
        global score 
        score +=1
        
        label.config(text="Score:{}".format(score))
        
        canvas.delete("food")
        
        food = Food()
        
    else:
        del snake.coordinate[-1]
    
        canvas.delete(snake.square[-1])

        del snake.square[-1]   
        
    if Check_collision(snake):
        Game_over()
    
    else:
    
        window.after(SPEED, Next_turn ,snake , food)
        
        
def Change_direction(new_direction):

    global direction
    
    if new_direction == 'left':
        if direction != 'right':
            direction= new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction= new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction= new_direction
    elif new_direction == 'down':
            if direction != 'up':
                direction= new_direction

def Check_collision(snake):
    
    x , y = snake.coordinate[0]
    
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinate[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
        
    
    return False  
    
def Game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                        font=('consolas',70), text="GAME OVER", fill="red", tag="Game_over")


window = Tk()
window.title("SNAKE  GAME")
window.resizable(False,False)

score= 0
direction= "down"

label=Label(window, text="score:{}".format(score), font=("consolas",40))
label.pack()

canvas=Canvas(window, bg=BACKGROUND_COLOR , height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.bind('<Left>' , lambda event: Change_direction('left'))
window.bind('<Right>', lambda event: Change_direction('right'))
window.bind('<Up>' , lambda event: Change_direction('up'))
window.bind('<Down>', lambda event: Change_direction('down'))

snake=Snake()

food=Food()

Next_turn(snake,food)

window.mainloop()