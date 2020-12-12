# WhatsApp-Formatter is a program that takes exported WhatsApp chats and
# formats them into more readable HTML files, with embedded attachments.
#
# Copyright (C) 2020 Doctor Dalek <https://github.com/DoctorDalek1963>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""PLAN:
- Button to add current data to list (clear data on press as well)
- Button to process allChatsList (call process_list(allChatsList) in a separate thread;
set startProcessingFlag; when thread is done, set endProcessingFlag)

- if startProcessingFlag:
    start new thread for process_all_chats()
    startProcessingFlag = False
    disable exit button
    display 'Formatting...' text
    clear allChatsList (disables format button because it's only enabled
        when allChatsLists has data)

- if endProcessingFlag:
    endProcessingFlag = False
    enable exit button
    remove 'Formatting...' text
"""


from formatter_functions import process_list
from tkinter import filedialog, StringVar
import tkinter as tk
import threading
import os

cwd = os.getcwd()
inputZip = outputDir = recipientName = ""
endProcessingFlag = startProcessingFlag = False
allChatsList = []

descriptionText = """Steps:\n
1. Select an exported chat\n
2. Select an export directory\n
3. Enter the name of the recipient (case sensitive)\n
4. Click the 'Add to list' button\n
5. Repeat steps 1-4 until you have selected all your chats\n
6. Click the 'Format' button\n
7. Wait until the 'Formatting...' text disappears\n
8. This may take quite a while if you've selected several large chats\n
9. Once the 'Exit' button is active, you can safely exit the program"""

default_x_padding = 10
default_y_padding = 5

# ===== Functions to be used on tk buttons


def select_zip():
    global inputZip
    inputZip = filedialog.askopenfilename(initialdir=cwd, title="Select an exported chat",
                                          filetypes=[("Zip files", "*.zip")])


def select_output_dir():
    global outputDir
    outputDir = filedialog.askdirectory(initialdir="/", title="Select an output directory")


def add_to_list():
    allChatsList.append([inputZip, recipientName, outputDir])


def start_processing():
    global startProcessingFlag
    startProcessingFlag = True


def process_all_chats():
    global endProcessingFlag
    endProcessingFlag = True
    process_list(allChatsList)


# ===== Tkinter initialisation

# Init window
root = tk.Tk()
root.title("WhatsApp Formatter")
root.resizable(False, False)

selected_zip_var = StringVar()
selected_output_var = StringVar()
formatting_string_var = StringVar()


# ===== Create widgets

# Create padding widgets
# middle_column_padding = tk.LabelFrame(root)
# row_padding_1 = tk.LabelFrame(root)
# row_padding_2 = tk.LabelFrame(root)
# row_padding_3 = tk.LabelFrame(root)
# row_padding_4 = tk.LabelFrame(root)

# Create input widgets
select_zip_button = tk.Button(root, text="Select an exported chat", command=select_zip)
selected_zip_label = tk.Label(root, textvariable=selected_zip_var)

select_output_button = tk.Button(root, text="Select an output directory", command=select_output_dir)
selected_output_label = tk.Label(root, textvariable=selected_output_var)

name_box_label = tk.Label(root, text="Enter the name of the recipient:")
enter_name_box = tk.Entry(root)

# Instructions for use
description_label = tk.Label(root, text=descriptionText)

# Create special button widgets
add_to_list_button = tk.Button(root, text="Add to list", command=add_to_list, state="disabled", bd=3)
format_button = tk.Button(root, text="Format", command=start_processing, state="disabled", bd=3)
formatting_string_label = tk.Label(root, textvariable=formatting_string_var)
exit_button = tk.Button(root, text="Exit", command=root.destroy, bd=3)


# ===== Place widgets

# Instructions for use
description_label.grid(row=0, rowspan=8, column=0, pady=default_y_padding,
                       padx=(default_x_padding, 30))

# Select zip and display name
select_zip_button.grid(row=0, column=2, padx=default_x_padding, pady=default_y_padding)
selected_zip_label.grid(row=1, column=2, padx=default_x_padding, pady=(default_y_padding, 15))

# Select output directory and display it
select_output_button.grid(row=2, column=2, padx=default_x_padding, pady=default_y_padding)
selected_output_label.grid(row=3, column=2, padx=default_x_padding, pady=(default_y_padding, 25))

# Place special button widgets
add_to_list_button.grid(row=4, column=2, padx=default_x_padding, pady=default_y_padding)
format_button.grid(row=5, column=2, padx=default_x_padding, pady=default_y_padding)
formatting_string_label.grid(row=6, column=2, padx=default_x_padding, pady=default_y_padding)
exit_button.grid(row=7, column=2, padx=default_x_padding, pady=default_y_padding)
#
