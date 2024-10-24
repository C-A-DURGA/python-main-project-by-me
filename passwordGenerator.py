import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_var.get()
    
    # Check if length is valid
    if not length.isdigit() or int(length) < 1:
        messagebox.showwarning("Invalid Input", "Please enter a valid length.")
        return
    
    length = int(length)

    # Determine character set
    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("No Selection", "Please select at least one character type.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(entry_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Initialize Tkinter window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x400")
window.resizable(False, False)

# Title label
label_title = tk.Label(window, text="Password Generator", font=("Arial", 18))
label_title.pack(pady=20)

# Length label and entry
label_length = tk.Label(window, text="Password Length:", font=("Arial", 12))
label_length.pack()

length_var = tk.StringVar()
entry_length = tk.Entry(window, textvariable=length_var, width=10, font=("Arial", 12))
entry_length.pack(pady=5)

# Checkbuttons for character types
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

check_upper = tk.Checkbutton(window, text="Include Uppercase (A-Z)", variable=var_upper, font=("Arial", 10))
check_upper.pack(anchor="w", padx=30, pady=5)

check_lower = tk.Checkbutton(window, text="Include Lowercase (a-z)", variable=var_lower, font=("Arial", 10))
check_lower.pack(anchor="w", padx=30, pady=5)

check_digits = tk.Checkbutton(window, text="Include Digits (0-9)", variable=var_digits, font=("Arial", 10))
check_digits.pack(anchor="w", padx=30, pady=5)

check_symbols = tk.Checkbutton(window, text="Include Symbols (@, #, $, etc.)", variable=var_symbols, font=("Arial", 10))
check_symbols.pack(anchor="w", padx=30, pady=5)

# Button to generate password
btn_generate = tk.Button(window, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_generate.pack(pady=20)

# Entry to display the generated password
entry_password = tk.Entry(window, width=30, font=("Arial", 14), justify="center")
entry_password.pack(pady=10)

# Button to copy password to clipboard
btn_copy = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#008CBA", fg="white")
btn_copy.pack(pady=10)

# Start the Tkinter loop
window.mainloop()
