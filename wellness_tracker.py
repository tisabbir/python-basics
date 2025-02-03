import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Daily Wellness Tracker")

# Create Tabs
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Log Activity')
tabControl.add(tab2, text='View Progress')
tabControl.pack(expand=1, fill="both")

# Tab 1 Content
ttk.Label(tab1, text="Meals:", padding=10).grid(column=0, row=0)
ttk.Entry(tab1).grid(column=1, row=0)

ttk.Label(tab1, text="Water Intake (oz):", padding=10).grid(column=0, row=1)
ttk.Entry(tab1).grid(column=1, row=1)

# ... Add more input fields ...

root.mainloop()
