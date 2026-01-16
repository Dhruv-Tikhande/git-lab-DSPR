import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Main window
root = tk.Tk()
root.title("Simple Maths Calculator")
root.geometry("300x350")

# Heading
tk.Label(root, text="Maths Calculator", font=("Arial", 16)).pack(pady=10)

# Number 1
tk.Label(root, text="Enter Number 1").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

# Number 2
tk.Label(root, text="Enter Number 2").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Buttons
tk.Button(root, text="Add (+)", width=15, command=lambda: calculate("+")).pack(pady=5)
tk.Button(root, text="Subtract (-)", width=15, command=lambda: calculate("-")).pack(pady=5)
tk.Button(root, text="Multiply (*)", width=15, command=lambda: calculate("*")).pack(pady=5)
tk.Button(root, text="Divide (/)", width=15, command=lambda: calculate("/")).pack(pady=5)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack(pady=15)

# Run app
root.mainloop()
