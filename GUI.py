import sys
import tkinter as tk
import tkinter.scrolledtext as tkst
import os
from page_reader import page_reader
from data_extend import collect_details
from find_latest import get_newest_data, get_newest_extended_data
from list_gym_name_address import list_gyms

class Gym_hadler_GUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI for handling GYM lessons, lesson selectors, tibetable links.")

        self.new_list_button = tk.Button(master, text="Refresh GYM list from AYCM page", command=self.get_new_gym_list)
        self.new_list_button.pack()

        self.update_list_button = tk.Button(master, text="Collect GYM details from AYCM subpages", command=self.collect_links)
        self.update_list_button.pack()

        self.show_list_button = tk.Button(master, text="Show list of GYMs (extended)", command=self.show_gyms)
        self.show_list_button.pack()

        self.timetable_status_button = tk.Button(master, text="Check timetable status", command=self.check_timetable_status)
        self.timetable_status_button.pack()

        self.clear_button = tk.Button(master, text="Clear text", command=self.clear_text_field)
        self.clear_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        sys.exit

    def get_new_gym_list(self):
        gym_list = page_reader()
        edit_space.insert('insert',gym_list)

    def collect_links(self):
        updated_list = collect_details()
        edit_space.insert('insert',updated_list)

    def show_gyms(self):
        list = list_gyms(get_newest_extended_data())
        edit_space.delete(1.0, tk.END)
        edit_space.insert('insert', list)

    def check_timetable_status(self):
        recent = get_newest_extended_data()

        pass

    def clear_text_field(self):
        edit_space.delete(1.0, tk.END)


root = tk.Tk()

root.geometry("800x500")
root.title("ScrolledText")
frame = tk.Frame(root, bg='brown')
frame.pack(fill='both', expand='yes')
edit_space = tkst.ScrolledText(
    master = frame,
    wrap   = 'word',  # wrap text at full words only
    width  = 25,      # characters
    height = 10,      # text lines
    bg='beige'        # background color of edit area
)

on_start_text = "Last scanned for GYMs: " + get_newest_data() + "\n" + \
    "Last updated for details: " + get_newest_extended_data() + "\n"
# the padx/pady space will form a frame
edit_space.pack(fill='both', expand=True)
edit_space.insert('insert', on_start_text)

my_gui = Gym_hadler_GUI(root)

root.mainloop()