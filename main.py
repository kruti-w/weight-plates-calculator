import tkinter as tk
from tkinter import *
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Barbell Weights Configuration")
    root.geometry("800x800")

    frm = ttk.Frame(root, height=100, width=700, borderwidth=10)
    style = ttk.Style()
    style.configure("TFrame", background="green")
    frm.grid()
    ttk.Label(frm, text="Users: ").grid(column=3, row=5)
    editUsersBtn = ttk.Button(frm, text="EDIT")
    editUsersBtn.grid(column=690, row=5)
    editPlatesBtn = ttk.Button(frm, text="EDIT")
    editPlatesBtn.grid(column=690, row=15)

    ttk.Label(frm, text="Plates: ").grid(column=3, row=15)

    frm2 = ttk.Frame(root, height=300, width=700)
    frm2.grid()




    root.mainloop()


if __name__ == "__main__":
    main()
