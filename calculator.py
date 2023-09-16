import tkinter as tk

def click_button(button_text):
    current_text = entry_var.get()
    new_text = current_text + button_text
    entry_var.set(new_text)

def clear_entry():
    entry_var.set("")

def calculate():
    expression = entry_var.get()
    try:
        result = str(eval(expression))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display the input and result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Helvetica', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button_text in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20, font=('Helvetica', 14), command=lambda text=button_text: click_button(text)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear and equal buttons
tk.Button(root, text="C", padx=20, pady=20, font=('Helvetica', 14), command=clear_entry).grid(row=5, column=0)
tk.Button(root, text="=", padx=20, pady=20, font=('Helvetica', 14), command=calculate).grid(row=5, column=1, columnspan=3)

root.mainloop()