import os, shutil, time,sys
import tkinter as tk
from tkinter import *
root = Tk()
root.title("UNO Score keeper")
global countwinp1
global countwinp2
countwinp1 = 0
countwinp2 = 0
def player1nameChang():
    def player1nameE1():
        player1name['text'] = E1.get()
        top1.destroy()
    top1 = Tk()
    E1 = Entry(top1)
    enterdname1 = Button(top1, text = 'Done', command = player1nameE1)
    E1.pack()
    enterdname1.pack()
def player2nameChang():
    def player2nameE2():
        player2name['text'] = E2.get()
        top2.destroy()
    top2 = Tk()
    E2 = Entry(top2)
    enterdname2 = Button(top2, text = 'Done', command = player2nameE2)
    E2.pack()
    enterdname2.pack()   
def P1win():
    global countwinp1
    countwinp1 +=1
    p1wincount['text']=countwinp1
    print(countwinp1)
    global expression
    global tolalnow
    expression = ""
    top3 = Tk() 
    top3.title("score Calqleter") 
    equation =  StringVar()
    equation.set('click the cards to add') 
    display = Label(top3, text = '')
    tolalnow = Label(top3, text = '')
    tolalnow.grid(row = 0, column = 4)
    display.grid(row = 0, column = 0) 
    def press(num):
        global expression
        expression = expression + str(num)
        display['text'] = expression
    def equalpress(): 
        try: 
            global expression 
            global tolalnow
            global total
            total = str(eval(expression[:-1])) 
            tolalnow['text'] = str(eval(expression[:-1]))
            expression = "" 
        except: 
            equation.set(" error ") 
            expression = "" 
    def clear(): 
        global expression 
        expression = "" 
        equation.set("")  
    def player1calkill():
        global total
        holow = int(total) + int(player1ScoreBored['text'])
        player1ScoreBored ['text'] = holow
        top3.destroy()
    button1 = Button(top3, text=' Card1 ', fg='black', bg='red', 
                    command=lambda: [press(1),press("+")], height=7, width=7) 
    button1.grid(row=2, column=0) 
    button2 = Button(top3, text=' Card2 ', fg='black', bg='red', 
                    command=lambda: [press(2),press("+")], height=7, width=7) 
    button2.grid(row=2, column=1) 
    button3 = Button(top3, text=' Card3 ', fg='black', bg='red', 
                    command=lambda: [press(3),press("+")], height=7, width=7) 
    button3.grid(row=2, column=2) 
    button4 = Button(top3, text=' Card4 ', fg='black', bg='red', 
                    command=lambda: [press(4),press("+")], height=7, width=7) 
    button4.grid(row=2, column=3) 
    button5 = Button(top3, text=' Card5 ', fg='black', bg='red', 
                    command=lambda: [press(5),press("+")], height=7, width=7) 
    button5.grid(row=2, column=4) 
    button6 = Button(top3, text=' Card6 ', fg='black', bg='red', 
                    command=lambda: [press(6),press("+")], height=7, width=7) 
    button6.grid(row=3, column=0) 
    button7 = Button(top3, text=' Card7 ', fg='black', bg='red', 
                    command=lambda: [press(7),press("+")], height=7, width=7) 
    button7.grid(row=3, column=1) 
    button8 = Button(top3, text=' Card8 ', fg='black', bg='red', 
                    command=lambda: [press(8),press("+")], height=7, width=7) 
    button8.grid(row=3, column=2) 
    button9 = Button(top3, text=' Card9 ', fg='black', bg='red', 
                    command=lambda: [press(9),press("+")], height=7, width=7) 
    button9.grid(row=3, column=3) 
    button0 = Button(top3, text=' Card0 ', fg='black', bg='red', 
                    command=lambda: [press(0),press("+")], height=7, width=7) 
    button0.grid(row=3, column=4) 
    Decimal= Button(top3, text='+2', fg='black', bg='red', 
                    command=lambda: [press(20),press("+")], height=7, width=7) 
    Decimal.grid(row=4, column=0)
    minus = Button(top3, text='Revars', fg='black', bg='red', 
                command=lambda: [press(20),press("+")], height=7, width=7) 
    minus.grid(row=4, column=1) 
    multiply = Button(top3, text='skip', fg='black', bg='red', 
                    command=lambda: [press(20),press("+")], height=7, width=7) 
    multiply.grid(row=4, column=2) 
    divide = Button(top3, text='Wild/+4', fg='black', bg='red', 
                    command=lambda: [press(50),press("+")], height=7, width=7) 
    divide.grid(row=4, column=3) 
    equal = Button(top3, text=' = ', fg='black', bg='red', 
                command=equalpress, height=7, width=7) 
    equal.grid(row=5, column=2) 
    clear = Button(top3, text='Clear', fg='black', bg='red', 
                command=clear, height=7, width=7) 
    clear.grid(row=5, column=0) 
    plus = Button(top3, text='Dane', fg='black', bg='red',command=player1calkill, height=7, width=7) 
    plus.grid(row=5, column=4)
    top3.mainloop()   
def P2win():
    global countwinp2
    countwinp2 +=1
    p2wincount['text']=countwinp2
    global expression
    global tolalnow
    expression = ""
    top3 = Tk() 
    top3.title("score Calqleter") 
    equation =  StringVar()
    equation.set('click the cards to add') 
    display = Label(top3, text = '')
    tolalnow = Label(top3, text = '')
    tolalnow.grid(row = 0, column = 4)
    display.grid(row = 0, column = 0) 
    def press(num):
        global expression
        expression = expression + str(num)
        display['text'] = expression
    def equalpress(): 
        try: 
            global expression 
            global tolalnow
            global total
            total = str(eval(expression[:-1])) 
            tolalnow['text'] = str(eval(expression[:-1]))
            expression = "" 
        except: 
            equation.set(" error ") 
            expression = "" 
    def clear(): 
        global expression 
        expression = "" 
        equation.set("")  
    def player1calkill():
        global total
        holow = int(total) + int(player2ScoreBored['text'])
        player2ScoreBored ['text'] = holow
        top3.destroy()
    button1 = Button(top3, text=' Card1 ', fg='black', bg='red', 
                    command=lambda: [press(1),press("+")], height=7, width=7) 
    button1.grid(row=2, column=0) 
    button2 = Button(top3, text=' Card2 ', fg='black', bg='red', 
                    command=lambda: [press(2),press("+")], height=7, width=7) 
    button2.grid(row=2, column=1) 
    button3 = Button(top3, text=' Card3 ', fg='black', bg='red', 
                    command=lambda: [press(3),press("+")], height=7, width=7) 
    button3.grid(row=2, column=2) 
    button4 = Button(top3, text=' Card4 ', fg='black', bg='red', 
                    command=lambda: [press(4),press("+")], height=7, width=7) 
    button4.grid(row=2, column=3) 
    button5 = Button(top3, text=' Card5 ', fg='black', bg='red', 
                    command=lambda: [press(5),press("+")], height=7, width=7) 
    button5.grid(row=2, column=4) 
    button6 = Button(top3, text=' Card6 ', fg='black', bg='red', 
                    command=lambda: [press(6),press("+")], height=7, width=7) 
    button6.grid(row=3, column=0) 
    button7 = Button(top3, text=' Card7 ', fg='black', bg='red', 
                    command=lambda: [press(7),press("+")], height=7, width=7) 
    button7.grid(row=3, column=1) 
    button8 = Button(top3, text=' Card8 ', fg='black', bg='red', 
                    command=lambda: [press(8),press("+")], height=7, width=7) 
    button8.grid(row=3, column=2) 
    button9 = Button(top3, text=' Card9 ', fg='black', bg='red', 
                    command=lambda: [press(9),press("+")], height=7, width=7) 
    button9.grid(row=3, column=3) 
    button0 = Button(top3, text=' Card0 ', fg='black', bg='red', 
                    command=lambda: [press(0),press("+")], height=7, width=7) 
    button0.grid(row=3, column=4) 
    Decimal= Button(top3, text='+2', fg='black', bg='red', 
                    command=lambda: [press(20),press("+")], height=7, width=7) 
    Decimal.grid(row=4, column=0)
    minus = Button(top3, text='Revars', fg='black', bg='red', 
                command=lambda: [press(20),press("+")], height=7, width=7) 
    minus.grid(row=4, column=1) 
    multiply = Button(top3, text='skip', fg='black', bg='red', 
                    command=lambda: [press(20),press("+")], height=7, width=7) 
    multiply.grid(row=4, column=2) 
    divide = Button(top3, text='Wild/+4', fg='black', bg='red', 
                    command=lambda: [press(50),press("+")], height=7, width=7) 
    divide.grid(row=4, column=3) 
    equal = Button(top3, text=' = ', fg='black', bg='red', 
                command=equalpress, height=7, width=7) 
    equal.grid(row=5, column=2) 
    clear = Button(top3, text='Clear', fg='black', bg='red', 
                command=clear, height=7, width=7) 
    clear.grid(row=5, column=0) 
    plus = Button(top3, text='Dane', fg='black', bg='red',command=player1calkill, height=7, width=7) 
    plus.grid(row=5, column=4)
    top3.mainloop()   
player1Score = Label(root, width=10, text = 'Score')
player1ScoreBored = Label(root, width=10, text = '000')
changname1 = Button(root, text = 'enter Name P1', command=player1nameChang)
enterScoreP1 = Button(root, text = 'Win', command=P1win)
p1wincount = Label(root, text = str(countwinp1))
player2Score = Label(root, width=10, text = 'Score')
player2ScoreBored = Label(root, width=10, text = '000')
changname2 = Button(root, text = 'enter Name P2', command=player2nameChang)
enterScoreP2 = Button(root, text = 'Win', command=P2win)
p2wincount = Label(root, text = str(countwinp2))
player1name = Label(root, width=10, text = 'Player1')
changname1.grid(row = 0, column = 0)
player1name.grid(row = 1, column = 0)
player1Score.grid(row = 2, column = 0)
player1ScoreBored.grid(row = 3, column = 0)
enterScoreP1.grid(row = 4, column = 0)
p1wincount.grid(row = 5, column = 0)
player2name = Label(root, width=10, text = 'Player2')
changname2.grid(row = 0, column = 1)
player2name.grid(row = 1, column = 1)
player2Score.grid(row = 2, column = 1)
player2ScoreBored.grid(row = 3, column = 1)
enterScoreP2.grid(row = 4, column = 1)
p2wincount.grid(row = 5, column =1) 
root.mainloop()