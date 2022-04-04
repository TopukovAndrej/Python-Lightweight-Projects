"""
A simple script for generating passwords with GUI
"""
import random
from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import messagebox
from tkinter import END
from string import punctuation


def generate_button_click():
    """
    Validates the user input and generates passwords accordingly.
    If input(s) is/are invalid, an error message is shown.

    :returns: None
    """
    text_box_5.delete(1.0, END)
    text_box_6.delete(1.0, END)

    uppercase = text_box_1.get('1.0', 'end-1c')
    lowercase = text_box_2.get('1.0', 'end-1c')
    digits = text_box_3.get('1.0', 'end-1c')
    sp_chars = text_box_4.get('1.0', 'end-1c')

    try:
        uppercase = int(uppercase)
    except ValueError:
        messagebox.showerror(title='Error', message='Invalid input for number of uppercase letters!')
        return None
    try:
        lowercase = int(lowercase)
    except ValueError:
        messagebox.showerror(title='Error', message='Invalid input for number of lowercase letters!')
        return None
    try:
        digits = int(digits)
    except ValueError:
        messagebox.showerror(title='Error', message='Invalid input for number of digits!')
        return None
    try:
        sp_chars = int(sp_chars)
    except ValueError:
        messagebox.showerror(title='Error', message='Invalid input for number of special characters!')
        return None

    if uppercase < 0 or lowercase < 0 or digits < 0 or sp_chars < 0:
        messagebox.showerror(title='Error', message='Number of characters input cannot be less than zero!')
        return None

    uppercase_letters = [chr(i) for i in range(65, 91)]
    lowercase_letters = [chr(i) for i in range(97, 123)]
    digits_list = [str(i) for i in range(0, 10)]
    special_characters = list(punctuation)

    l1 = random.choices(population=uppercase_letters, k=uppercase)
    l2 = random.choices(population=lowercase_letters, k=lowercase)
    l3 = random.choices(population=digits_list, k=digits)
    l4 = random.choices(population=special_characters, k=sp_chars)

    result = l1 + l2 + l3 + l4
    random.shuffle(result)

    text_box_5.insert(index=END, chars=''.join(result))
    text_box_6.insert(index=END, chars=str(len(result)))

    return None


if __name__ == '__main__':
    form = Tk()
    form.wm_title('Password Generator')
    form.geometry('300x300')

    label_1 = Label(master=form, text='Enter number of uppercase letters:')
    label_1.place(x=1, y=10)

    text_box_1 = Text(master=form, height=1, width=8)
    text_box_1.place(x=200, y=10)

    label_2 = Label(master=form, text='Enter number of lowercase letters:')
    label_2.place(x=1, y=40)

    text_box_2 = Text(master=form, height=1, width=8)
    text_box_2.place(x=200, y=40)

    label_3 = Label(master=form, text='Enter number of digits:')
    label_3.place(x=1, y=70)

    text_box_3 = Text(master=form, height=1, width=8)
    text_box_3.place(x=200, y=70)

    label_4 = Label(master=form, text='Enter number of special characters:')
    label_4.place(x=1, y=100)

    text_box_4 = Text(master=form, height=1, width=8)
    text_box_4.place(x=200, y=100)

    button = Button(master=form, height=1, width=10, text='Generate', command=generate_button_click)
    button.place(x=110, y=160)

    label_5 = Label(master=form, text='Generated password:')
    label_5.place(x=1, y=220)

    text_box_5 = Text(master=form, height=1, width=20)
    text_box_5.place(x=118, y=220)

    label_6 = Label(master=form, text='Generated password length:')
    label_6.place(x=1, y=260)

    text_box_6 = Text(master=form, height=1, width=7)
    text_box_6.place(x=154, y=260)

    form.mainloop()
