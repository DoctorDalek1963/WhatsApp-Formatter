from formatter_functions import *
import tkinter as tk
from tkinter import filedialog
import os

cwd = os.getcwd()
input_zip = outputDir = recipName = ""
finish_export_flag = start_export_flag = False

description_text = """Steps:\n
1. Select an exported chat\n
2. Select an export directory\n
3. Enter the name of the recipient (case sensitive)\n
4. Click the format button\n
5. Wait until the exit button is active\n
6. Click it to exit"""

default_x_padding = 10
default_y_padding = 5


# ===== Functions used on tk buttons


def select_zip():
    global input_zip
    input_zip = filedialog.askopenfilename(initialdir=cwd, title="Select an exported chat",
                                           filetypes=[("Zip files", "*.zip")])


def select_output_dir():
    global outputDir
    outputDir = filedialog.askdirectory(initialdir="/", title="Select an output directory")


def begin_export():
    global start_export_flag, finish_export_flag
    start_export_flag = True
    extract_zip(input_zip)
    write_to_file(recipName, outputDir)
    finish_export_flag = True


# ===== Tkinter initialisation

# Initialisation of window
root = tk.Tk()
root.title("WhatsApp Formatter")
root.resizable(False, False)

# Create widgets
middle_column_padding = tk.LabelFrame(root)
row_padding_1 = tk.LabelFrame(root)
row_padding_2 = tk.LabelFrame(root)
select_zip_button = tk.Button(root, text="Select an exported chat", command=select_zip, bd=3)
select_output_button = tk.Button(root, text="Select an output directory", command=select_output_dir, bd=3)
name_box_label = tk.Label(root, text="Enter the name of the recipient:")
enter_name_box = tk.Entry(root)
description_label = tk.Label(root, text=description_text)

# Create special widgets
format_button = tk.Button(root, text="Format", command=begin_export, state="disabled", bd=3)
exit_button = tk.Button(root, text="Exit", command=root.destroy, state="disabled", bd=3)

# Place widgets
middle_column_padding.grid(row=2, column=1, padx=20)
row_padding_1.grid(row=4, column=2, pady=15)
select_zip_button.grid(row=2, column=2, pady=default_y_padding, padx=default_x_padding)
select_output_button.grid(row=3, column=2, pady=default_y_padding, padx=default_x_padding)
name_box_label.grid(row=5, column=2, pady=default_y_padding, padx=default_x_padding)
enter_name_box.grid(row=6, column=2, pady=default_y_padding, padx=default_x_padding)

description_label.grid(row=1, rowspan=9, column=0, pady=default_y_padding, padx=default_x_padding)
row_padding_2.grid(row=7, column=2, pady=15)

# Place special widgets
format_button.grid(row=8, column=2, pady=default_y_padding, padx=default_x_padding)
exit_button.grid(row=9, column=2, pady=15, padx=5)

# ===== Loop to sustain window

# Infinite loop to update tk window and check for conditions to activate or deactivate buttons
while True:
    recipName = enter_name_box.get()

    if input_zip and outputDir and recipName:
        format_button.config(state="normal")

    if start_export_flag:
        format_button.config(state="disabled")

    if finish_export_flag:
        exit_button.config(state="normal")

    root.update()
