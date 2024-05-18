import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import *
import json
# https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file

with open('data.json', 'r') as data_file:
    data_loaded = json.load(data_file)

print(f"{data_loaded=}")

p_list = []
u_list = []

p_list, u_list = data_loaded

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
    print("program closing")
    with open('data.json', 'w') as txtfile:
        json.dump([p_list, u_list], txtfile)
        # json.dump("\n", txtfile)
        # json.dump(u_list, txtfile)
    print("Json done")

if __name__ == "__main__":
    main()
