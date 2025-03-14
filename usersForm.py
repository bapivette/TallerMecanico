import tkinter as tk
from tkinter import messagebox
from db.dbUsuario import DbUsuario

class UsersWindow:
    def __init__(self, root, user):
        self.root = root
        self.root.title("Users - Taller Mecanico")
        self.user = user
        self.db_user = DbUsuario()

        self.id_label = tk.Label(self.root, text="Enter User ID:")
        self.id_label.pack()

        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        self.search_button = tk.Button(self.root, text="Search", command=self.search_user)
        self.search_button.pack()

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.perfil_label = tk.Label(self.root, text="Perfil:")
        self.perfil_label.pack()

        self.perfil_entry = tk.Entry(self.root)
        self.perfil_entry.pack()

        self.save_button = tk.Button(self.root, text="Save", command=self.save_user)
        self.save_button.pack()

        self.edit_button = tk.Button(self.root, text="Edit", command=self.edit_user)
        self.edit_button.pack()

        self.remove_button = tk.Button(self.root, text="Remove", command=self.remove_user)
        self.remove_button.pack()

    def search_user(self):
        usuario_id = self.id_entry.get()
        if usuario_id:
            user = self.db_user.search(usuario_id)
            if user:
                self.username_entry.delete(0, tk.END)
                self.username_entry.insert(0, user['username'])
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, user['password'])
                self.perfil_entry.delete(0, tk.END)
                self.perfil_entry.insert(0, user['perfil'])
            else:
                messagebox.showerror("Error", "User not found.")

    def save_user(self):
        usuario = {
            'nombre': self.username_entry.get(),
            'username': self.username_entry.get(),
            'password': self.password_entry.get(),
            'perfil': self.perfil_entry.get()
        }
        self.db_user.save(usuario)
        messagebox.showinfo("Success", "User saved successfully.")

    def edit_user(self):
        usuario = {
            'usuario_id': self.id_entry.get(),
            'nombre': self.username_entry.get(),
            'username': self.username_entry.get(),
            'password': self.password_entry.get(),
            'perfil': self.perfil_entry.get()
        }
        self.db_user.edit(usuario)
        messagebox.showinfo("Success", "User updated successfully.")

    def remove_user(self):
        usuario_id = self.id_entry.get()
        self.db_user.remove(usuario_id)
        messagebox.showinfo("Success", "User removed successfully.")
