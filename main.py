import tkinter as tk
from tkinter import *
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Barbell Weights Configuration")
    root.geometry("800x800")

    frm = ttk.Frame(root, padding=250)
    frm.grid()
    ttk.Label(frm, text="Testing").grid(column=3, row=5)
    ttk.Label(frm, text="Testing").grid(column=10, row=5)
    root.mainloop()


if __name__ == "__main__":
    main()
