import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x600")
        self.root.config(bg="#f2f2f2")

        self.tasks = []

        # Header
        self.header = tk.Label(self.root, text="To-Do List", bg="#f2f2f2", fg="#333333", font=("Helvetica", 18, "bold"))
        self.header.pack(pady=20)

        # Task List Frame
        self.task_frame = tk.Frame(self.root, bg="#f2f2f2")
        self.task_frame.pack(pady=10)

        self.task_list = tk.Listbox(self.task_frame, width=45, height=15, font=("Helvetica", 12), bd=0, selectbackground="#a6a6a6", activestyle="none")
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, padx=10)

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        # Task Entry Frame
        self.task_entry_frame = tk.Frame(self.root, bg="#f2f2f2")
        self.task_entry_frame.pack(pady=20)

        self.task_entry = tk.Entry(self.task_entry_frame, font=("Helvetica", 12), width=30, bd=0)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_task_button = tk.Button(self.task_entry_frame, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="#4caf50", fg="#ffffff", padx=10, pady=5)
        self.add_task_button.pack(side=tk.LEFT, padx=10)

        self.delete_task_button = tk.Button(self.root, text="Delete Selected Task", command=self.delete_task, font=("Helvetica", 12), bg="#f44336", fg="#ffffff", padx=10, pady=5)
        self.delete_task_button.pack(pady=20)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_list.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
