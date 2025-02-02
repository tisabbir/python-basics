import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog


def write_numbers():
    try:
        n = int(entry.get())
        with open("NUM.txt", "w") as file:
            for i in range(n):
                number = simpledialog.askstring("Input", f"Enter number {i + 1}:")
                if number is not None and number.strip().isdigit():
                    file.write(number + "\n")
                else:
                    messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
                    return
        messagebox.showinfo("Success", "Numbers saved to NUM.txt")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


def calculate_average():
    try:
        with open("NUM.txt", "r") as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

        if numbers:
            total_sum = sum(numbers)
            avg = total_sum / len(numbers)
            result_label.config(text=f"Numbers: {numbers}\nSum: {total_sum}\nAverage: {avg:.2f}")
        else:
            result_label.config(text="No valid numbers in file.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")


root = tk.Tk()
root.title("Number File Handler")

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="How Many Numbers:").grid(row=0, column=0)
entry = tk.Entry(frame)
entry.grid(row=0, column=1)

tk.Button(frame, text="Write Numbers", command=write_numbers).grid(row=1, column=0, columnspan=2)
tk.Button(frame, text="Calculate Average", command=calculate_average).grid(row=2, column=0, columnspan=2)

result_label = tk.Label(root, text="Enter numbers and calculate average.")
result_label.pack()

root.mainloop()