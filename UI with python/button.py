import tkinter as tk

def on_click():
    label.config(text="Button Clicked")

root = tk.Tk()  # Corrected: tk.Tk() instead of tk.TK()
root.title("Basic GUI")

label = tk.Label(root, text="Hello World")  # Corrected: tk.Label instead of tk.label
label.pack()

button = tk.Button(root, text="This is CLICK", command=on_click)  # Corrected: command=on_click instead of command=on_click()
button.pack()

root.mainloop()