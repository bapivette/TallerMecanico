import tkinter as tk
from forms.users_form import UsersWindow

class MenuWindow:
    def __init__(self, root, user):
        self.root = root
        self.root.title("Menu - Taller Mecanico")
        self.user = user

        self.users_button = tk.Button(self.root, text="Users", command=self.open_users)
        self.users_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()

    def open_users(self):
        user_window = tk.Tk()
        user_interface = UsersWindow(user_window, self.user)
        user_window.mainloop()
