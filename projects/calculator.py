import tkinter as tk
from tkinter import font

# ফাংশনগুলি
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# মূল উইন্ডো তৈরি
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("400x600")
root.configure(bg="#2E3440")

# কালার স্কিম
bg_color = "#2E3440"
button_bg = "#3B4252"
button_fg = "#ECEFF4"
entry_bg = "#4C566A"
entry_fg = "#ECEFF4"

# ফন্ট সেটিং
button_font = font.Font(family="Helvetica", size=18, weight="bold")
entry_font = font.Font(family="Helvetica", size=32, weight="bold")

# এন্ট্রি বক্স
entry = tk.Entry(root, width=15, font=entry_font, bg=entry_bg, fg=entry_fg, borderwidth=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=20)

# বাটন তৈরি
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, font=button_font, bg="#BF616A", fg=button_fg, borderwidth=0, command=clear)
    elif text == '=':
        btn = tk.Button(root, text=text, font=button_font, bg="#A3BE8C", fg=button_fg, borderwidth=0, command=calculate)
    else:
        btn = tk.Button(root, text=text, font=button_font, bg=button_bg, fg=button_fg, borderwidth=0, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=10, pady=10, ipadx=20, ipady=20, sticky="nsew")

# কলাম এবং রো কনফিগারেশন
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# মূল ইভেন্ট লুপ
root.mainloop()