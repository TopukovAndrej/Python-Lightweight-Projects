import os
import tkinter as tk
import tkinter.ttk as ttk
from contact import Contact
from contact_book import ContactBook


if __name__ == '__main__':
    main_form = tk.Tk()
    main_form.wm_title('Contact Book')
    main_form.geometry('320x180')

    lb1 = tk.Label(master=main_form, text='Welcome to Contact Book!')
    lb1.place(x=77, y=20)

    style = ttk.Style()
    style.configure('Custom.TButton')

    btn1 = ttk.Button(master=main_form, text='Add new contact')
    btn1.place(x=100, y=50)

    btn2 = ttk.Button(master=main_form, text='Update existing contact')
    btn2.place(x=85, y=80)

    btn3 = ttk.Button(master=main_form, text='Delete contact')
    btn3.place(x=105, y=110)

    btn4 = ttk.Button(master=main_form, text='Quit')
    btn4.place(x=110, y=140)

    main_form.mainloop()
