import tkinter as tk
from tkinter import messagebox
from db.dbUsuario import DbUsuario

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Taller Mecanico")

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_db = DbUsuario()
        user = user_db.authenticate(username, password)

        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            self.open_menu(user)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def open_menu(self, user):
        menu_window = tk.Tk()
        menu = MenuWindow(menu_window, user)
        menu_window.mainloop()
