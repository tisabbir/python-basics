import tkinter as tk
from tkinter import ttk

# Define colors
BG_COLOR = "#16C47F"
BTN_COLOR1 = "#FFD65A"
BTN_COLOR2 = "#FF9D23"
BTN_COLOR3 = "#F93827"
TEXT_COLOR = "#FFFFFF"

# Create main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.config(bg=BG_COLOR)

# Entry widget to display expressions
expression = ""
def update_display(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear_display():
    global expression
    expression = ""
    display_var.set("")

def calculate_result():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""

# Display field
display_var = tk.StringVar()
display = ttk.Entry(root, textvariable=display_var, font=("Arial", 18), justify='right')
display.pack(fill='both', padx=10, pady=10, ipady=5)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Button frame
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(expand=True, fill='both')

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame, bg=BG_COLOR)
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn_color = BTN_COLOR1 if btn_text.isdigit() else BTN_COLOR2
        if btn_text in ['C', '=']:
            btn_color = BTN_COLOR3
        button = tk.Button(
            row_frame, text=btn_text, font=("Arial", 16), bg=btn_color, fg="black",
            relief='raised', bd=3, command=(lambda x=btn_text: update_display(x) if x not in ['C', '='] else clear_display() if x == 'C' else calculate_result())
        )
        button.pack(side='left', expand=True, fill='both', padx=5, pady=5)

# Run application
root.mainloop()
