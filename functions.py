from tkinter import *
from tkinter import ttk
import tkinter as tk
import json


def add_user(users_list):
    users_window = tk.Toplevel()
    users_window.title("Modify Users")
    users_window.geometry("450x450")

    label = tk.Label(users_window, text="All Users")
    for user in users_list:
        user_label = tk.Label(users_window, text=user)
        user_label.grid()
        delete_btn = Button(users_window, text="DELETE", command=lambda: delete_user())
        delete_btn.grid()

    label.grid()
    add_btn = tk.Button(users_window, text="ADD", command=lambda: add_new_user(users_list))
    add_btn.grid()


def add_new_user(user_list):
    add_new = tk.Toplevel()
    add_new.title("Add User")
    add_new.geometry("350x350")

    tk.Label(add_new, text="Name").grid(row=5)
    input_name = Entry(add_new)
    input_name.grid(row=5, column=10)
    print(input_name.get())

    def ok_func():
        print(f"Pressed OK.\nInput was {input_name.get()}")
        user_list.append(input_name.get())
        print(f"Updated {user_list=}")
        add_new.destroy()

    ok_btn = Button(add_new, text="OK", command=ok_func)
    ok_btn.grid(row=10)


def edit_users():
    return


def add_plates(plates_list):
    plates_window = tk.Toplevel()
    plates_window.title("Modify Plates")
    plates_window.geometry("450x450")

    label = tk.Label(plates_window, text="This is the list of all the plates you have")
    for plate in plates_list:
        plate_label = tk.Label(plates_window, text=plate)
        plate_label.grid()

        w = Spinbox(plates_window, from_=0, to=50)
        w.grid()

    label.grid()
    add_btn = tk.Button(plates_window, text="ADD", command=lambda: add_new_plates(plates_list))
    add_btn.grid()


def add_new_plates(plate_list):
    add_new = tk.Toplevel()
    add_new.title("Add New Plates")
    add_new.geometry("350x350")

    tk.Label(add_new, text="Weight (in lbs): ").grid(row=5)
    tk.Label(add_new, text="Quantity").grid(row=10)
    input_weight = Entry(add_new)
    input_weight.grid(row=5, column=10)
    input_quantity = Entry(add_new)
    input_quantity.grid(row=10, column=10)

    def ok_func():
        print(f"Pressed OK.\nInput was {input_quantity.get()}")
        plate_list.append([input_weight.get(), input_quantity.get()])
        print(f"Updated {plate_list=}")
        add_new.destroy()

    ok_btn = tk.Button(add_new, text="OK", command=ok_func)
    ok_btn.grid(row=16, column=10)


def edit_plates(plates_list):
    return


def output_plates():
    return


def delete_user():
    return


def delete_plate():
    return
