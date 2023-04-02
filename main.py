from tkinter import *
import random

prompt = 'Please pick rock, paper, or scissors.'
count = 0
x = 0
y = 0


def clickRock():

    list = ['rock','paper','scissors']
    prompt = random.choice(list)
    if prompt == 'rock':
        label.config(text=prompt + ' YOU TIED')
    elif prompt == 'paper':
        label.config(text=prompt + ' YOU LOSE')
    elif prompt == 'scissors':
        label.config(text=prompt + ' YOU WIN')
        global count
        count += 1
        label2.config(text=str(count) + ' wins')
    print(prompt)

def clickPaper():

    list = ['rock','paper','scissors']
    prompt = random.choice(list)
    if prompt == 'rock':
        label.config(text=prompt + ' YOU WIN')
        global count
        count += 1
        label2.config(text=str(count) + ' wins')
    elif prompt == 'paper':
        label.config(text=prompt + ' YOU TIED')
    elif prompt == 'scissors':
        label.config(text=prompt + ' YOU LOSE')
    print(prompt)

def clickScissors():

    list = ['rock','paper','scissors']
    prompt = random.choice(list)
    if prompt == 'rock':
        label.config(text=prompt + ' YOU LOSE')
    elif prompt == 'paper':
        label.config(text=prompt + ' YOU WIN')
        global count
        count +=1
        label2.config(text=str(count) + ' wins')
    elif prompt == 'scissors':
        label.config(text=prompt + ' YOU TIED')
    print(prompt)

def counter():
    global count
    count += 1
    label2.config(text=str(count) + ' games')

window = Tk()
window.title('Rock, Paper, Scissors Game')
window.geometry('1000x500')
button = Button(window, text='ROCK')
button.config(command=clickRock) #calls function
button.config(font=('Ink Free', 20, 'bold'))
button.config(bg='blue')
button.config(fg='white')
button.config(activebackground='green')
button.config(activeforeground='green')
button2 = Button(window, text='PAPER')
button2.config(command=clickPaper) #calls function
button2.config(font=('Ink Free', 20, 'bold'))
button2.config(bg='green')
button2.config(fg='white')
button2.config(activebackground='green')
button2.config(activeforeground='green')
button3 = Button(window, text='SCISSORS')
button3.config(command=clickScissors) #calls function
button3.config(font=('Ink Free', 20, 'bold'))
button3.config(bg='yellow')
button3.config(fg='black')
button3.config(activebackground='yellow')
button3.config(activeforeground='purple')
label = Label(window, text=prompt)
label.config(font=('Monospace', 35))
label.pack()
label2 = Label(window, text=count)
label2.config(font=('Monospace',35))
label2.pack()
button.pack()
button2.pack(pady=100)
button3.pack()
window.mainloop()

