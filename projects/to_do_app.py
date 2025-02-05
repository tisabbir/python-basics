import tkinter as tk

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
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)

        self.task_list = tk.Listbox(self.task_frame, width=45, height=15, font=("Helvetica", 12))
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        # Task Entry Frame
        self.task_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.task_entry.pack(pady=20)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="#333333", fg="#f2f2f2")
        self.add_task_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Warning", "You must enter a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
