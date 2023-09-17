import tkinter as tk
from tkinter import ttk


def calculate():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result.set(x + y)
        elif operation == "Subtraction":
            result.set(x - y)
        elif operation == "Multiplication":
            result.set(x * y)
        elif operation == "Division":
            if y == 0:
                result.set("Division by zero")
            else:
                result.set(x / y)
    except ValueError:
        result.set("Error")


# Create the main window
root = tk.Tk()
root.title("Elegant Calculator")
root.geometry("400x300")

# Create a frame for the calculator
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Create input fields and labels
label1 = ttk.Label(frame, text="Enter first number:")
label1.grid(row=0, column=0, pady=5)
entry1 = ttk.Entry(frame)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = ttk.Label(frame, text="Enter second number:")
label2.grid(row=1, column=0, pady=5)
entry2 = ttk.Entry(frame)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Create a dropdown for selecting the operation
operation_var = tk.StringVar()
operation_var.set("Addition")
operation_label = ttk.Label(frame, text="Select Operation:")
operation_label.grid(row=2, column=0, pady=5)
operation_menu = ttk.Combobox(frame, textvariable=operation_var,
                              values=["Addition", "Subtraction", "Multiplication", "Division"])
operation_menu.grid(row=2, column=1, padx=10, pady=5)

# Create a calculate button
calculate_button = ttk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2, pady=10)

# Display the result
result = tk.StringVar()
result_label = ttk.Label(frame, text="Result:")
result_label.grid(row=4, column=0, pady=5)
result_entry = ttk.Entry(frame, textvariable=result, state="readonly")
result_entry.grid(row=4, column=1, padx=10, pady=5)

# Configure grid weights to make the frame expandable
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)

# Run the GUI application
root.mainloop()
