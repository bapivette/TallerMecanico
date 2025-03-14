import tkinter as tk
from forms.login_form import LoginWindow

if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
