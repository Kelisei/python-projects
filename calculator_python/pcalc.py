from decimal import DivisionByZero
import tkinter as tk
from tkinter import font

expression = ""

root = tk.Tk()
root.title("PCalc")
root.geometry("400x500")
root.configure(bg="#181818")
custom_font = font.Font(family="Calibri", size=20, weight="normal")

def pressButton(value:str, entry:tk.Entry):
    global expression
    expression += value
    entry.delete(0, tk.END)
    entry.insert(0, expression)

def pressClear(entry):
    global expression
    expression = ""
    entry.delete(0, tk.END)
    entry.insert(0, expression)

def clearLast(entry):
    global expression
    expression = expression[0:len(expression)-1]
    entry.delete(0, tk.END)
    entry.insert(0, expression)

def pressResult(entry):
    global expression
    result = expression
    try:
        result = str(eval(expression))
        expression = result
    except SyntaxError: 
        result = "Syntax Error"
        expression = ""
    except ZeroDivisionError:
        result = "Can't divide by zero"
        expression = ""
    finally:
        entry.delete(0, tk.END)
        entry.insert(0, result)

entry = tk.Entry(width=50, font=custom_font)
entry.configure(bg="#202020", foreground="white")
entry.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
buttons = [
    [
        tk.Button(text="DIV", width=5, command= lambda: pressButton("//", entry), font=custom_font),
        tk.Button(text="MOD", width=5, command= lambda: pressButton("%", entry), font=custom_font),
        tk.Button(text="CLR", width=5, command= lambda: pressClear(entry), font=custom_font),
        tk.Button(text="<-", width=5, command= lambda: clearLast(entry), font=custom_font),
    ],
    [
        tk.Button(text="x^2", width=5, command= lambda: pressButton("**2", entry), font=custom_font),
        tk.Button(text="2√x", width=5, command= lambda: pressButton("**0.5", entry), font=custom_font),
        tk.Button(text="÷", width=5, command= lambda: pressButton("/", entry), font=custom_font),
        tk.Button(text=")", width=5, command= lambda: pressButton(")", entry), font=custom_font),
    ],
    [
        tk.Button(text="7", width=5, command= lambda: pressButton("7", entry), font=custom_font),
        tk.Button(text="8", width=5, command= lambda: pressButton("8", entry), font=custom_font),
        tk.Button(text="9", width=5, command= lambda: pressButton("9", entry), font=custom_font),
        tk.Button(text="×", width=5, command= lambda: pressButton("*", entry), font=custom_font),
    ],
    [
        tk.Button(text="4", width=5, command= lambda: pressButton("4", entry), font=custom_font),
        tk.Button(text="5", width=5, command= lambda: pressButton("5", entry), font=custom_font),
        tk.Button(text="6", width=5, command= lambda: pressButton("6", entry), font=custom_font),
        tk.Button(text="-", width=5, command= lambda: pressButton("-", entry), font=custom_font),
    ],
    [
        tk.Button(text="1", width=5, command= lambda: pressButton("1", entry), font=custom_font),
        tk.Button(text="2", width=5, command= lambda: pressButton("2", entry), font=custom_font),
        tk.Button(text="3", width=5, command= lambda: pressButton("3", entry), font=custom_font),
        tk.Button(text="+", width=5, command= lambda: pressButton("+", entry), font=custom_font),
    ],
    [
        tk.Button(text="(", width=5, command= lambda: pressButton("(", entry), font=custom_font),
        tk.Button(text="0", width=5, command= lambda: pressButton("0", entry), font=custom_font),
        tk.Button(text=",", width=5, command= lambda: pressButton(".", entry), font=custom_font),
        tk.Button(text="=", width=5, command= lambda: pressResult(entry), font=custom_font),
    ],
]

for i, buttonRow in enumerate(buttons):
    for j, button in enumerate(buttonRow):
        button.configure(bg="#303030", foreground="white")
        button.grid(row=i + 2, column=j, padx=4, pady=4, sticky="nsew")
        root.columnconfigure(j, weight=1)  # Make columns resizable
    root.rowconfigure(i + 2, weight=1)  # Make rows resizable

root.mainloop()
