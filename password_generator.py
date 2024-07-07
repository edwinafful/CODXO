import string
import random
import tkinter as tk
from tkinter import ttk, messagebox


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Frame for main content
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title label
        title_label = ttk.Label(main_frame, text="Secure Password Generator", font=("Helvetica", 18))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Password length
        length_label = ttk.Label(main_frame, text="Password Length:")
        length_label.grid(row=1, column=0, sticky=tk.W, pady=10)
        self.length_var = tk.IntVar(value=12)
        length_entry = ttk.Entry(main_frame, textvariable=self.length_var, width=5)
        length_entry.grid(row=1, column=1, sticky=tk.W, pady=10)

        # Character type checkboxes
        self.alphabets_var = tk.IntVar(value=1)
        alphabets_check = ttk.Checkbutton(main_frame, text="Include Alphabets", variable=self.alphabets_var)
        alphabets_check.grid(row=2, column=0, sticky=tk.W, pady=5)

        self.digits_var = tk.IntVar(value=1)
        digits_check = ttk.Checkbutton(main_frame, text="Include Digits", variable=self.digits_var)
        digits_check.grid(row=3, column=0, sticky=tk.W, pady=5)

        self.special_var = tk.IntVar(value=1)
        special_check = ttk.Checkbutton(main_frame, text="Include Special Characters", variable=self.special_var)
        special_check.grid(row=4, column=0, sticky=tk.W, pady=5)

        # Generate button
        generate_button = ttk.Button(main_frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Generated password label and entry
        password_label = ttk.Label(main_frame, text="Generated Password:")
        password_label.grid(row=6, column=0, sticky=tk.W, pady=5)
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, state='readonly')
        password_entry.grid(row=6, column=1, sticky=tk.W, pady=5)

    def generate_password(self):
        length = self.length_var.get()
        include_alphabets = self.alphabets_var.get()
        include_digits = self.digits_var.get()
        include_special = self.special_var.get()

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return

        if include_alphabets + include_digits + include_special == 0:
            messagebox.showerror("Error", "Select at least one character type to include.")
            return

        characters = []

        if include_alphabets:
            characters.extend(string.ascii_letters)

        if include_digits:
            characters.extend(string.digits)

        if include_special:
            characters.extend("!@#$%^&*()_+-=[]{}|;:,.<>?")

        # Generate password
        password = ''.join(random.choices(characters, k=length))
        
        # Shuffle password characters
        password_list = list(password)
        random.shuffle(password_list)
        shuffled_password = ''.join(password_list)

        self.password_var.set(shuffled_password)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
