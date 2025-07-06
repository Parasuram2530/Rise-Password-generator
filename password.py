import tkinter as tk
from tkinter import messagebox
import random

# Character groups
digits = [str(i) for i in range(10)]
lowercase = list("abcdefghijklmnopqrstuvwxyz")
uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

# Password generation logic
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Password length must be at least 4!")
            return
        
        password_chars = []
        for _ in range(length // 4):
            password_chars.append(random.choice(digits))
            password_chars.append(random.choice(lowercase))
            password_chars.append(random.choice(uppercase))
            password_chars.append(random.choice(symbols))

        # Fill remaining characters (if any)
        remaining = length - len(password_chars)
        all_chars = digits + lowercase + uppercase + symbols
        for _ in range(remaining):
            password_chars.append(random.choice(all_chars))

        random.shuffle(password_chars)
        password = ''.join(password_chars)
        result_var.set(password)
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

title = tk.Label(root, text="🔐 Random Password Generator", font=("Arial", 14, "bold"), bg="#f0f0f0")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

length_label = tk.Label(frame, text="Enter Password Length:", font=("Arial", 12), bg="#f0f0f0")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(frame, font=("Arial", 12), width=10)
length_entry.grid(row=0, column=1, padx=5, pady=5)

generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#007acc", fg="white", command=generate_password)
generate_btn.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Courier", 14), fg="#333", bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()



