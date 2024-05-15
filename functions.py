from tkinter import *
from tkinter import ttk
import tkinter as tk


def add_user(users_list):
    users_window = tk.Toplevel()
    users_window.title("Modify Users")
    users_window.geometry("450x450")

    label = tk.Label(users_window, text="View Users")
    for user in users_list:
        user_label = tk.Label(users_window, text=user)
        user_label.grid()

    label.grid()


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

    label.grid()


def edit_plates(plates_list):
    return


def output_plates():
    return


def delete_user():
    return


def delete_plate():
    return
