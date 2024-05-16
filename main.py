import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import *

p_list = ["0"]
u_list = ["User1", "User2"]


def main():
    root = tk.Tk()
    root.title("Barbell Weights Configuration")
    root.geometry("800x800")

    frm = ttk.Frame(root, height=100, width=700, borderwidth=10)
    style = ttk.Style()
    style.configure("TFrame", background="green")
    frm.grid()
    ttk.Label(frm, text="Users: ").grid(column=3, row=5)
    editUsersBtn = ttk.Button(frm, text="ADD OR EDIT", command=lambda: add_user(u_list))
    editUsersBtn.grid(column=690, row=5)
    editPlatesBtn = ttk.Button(frm, text="ADD OR EDIT", command=lambda: add_plates(p_list))
    editPlatesBtn.grid(column=690, row=15)

    ttk.Label(frm, text="Plates: ").grid(column=3, row=15)

    frm2 = ttk.Frame(root, height=300, width=700)
    frm2.grid()
    frm2.grid_propagate(False)

    input_str1 = tk.Entry(frm2)
    input_str1.grid(column=10, row=25)

    root.mainloop()


if __name__ == "__main__":
    main()
