"""
A simple binary/decimal converter script with GUI
"""
from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import messagebox
from tkinter import LEFT
from tkinter import RIGHT
from tkinter import END
from tkinter import StringVar
from tkinter import OptionMenu


def convert_binary_to_decimal(binary_number: str):
    """
    Converts the binary number to decimal number

    :param binary_number: a binary number
    :type binary_number: str
    :return: the number in decimal numeral system
    """
    num = 0

    i = 0
    for digit in binary_number[::-1]:
        try:
            digit = int(digit)
        except ValueError:
            messagebox.showerror(title='Error', message='Invalid character in binary number (currently only positive '
                                                        'numbers can be converted)!')
            return None
        num += digit * pow(2, i)
        i += 1

    return str(num)


def convert_decimal_to_binary(decimal_number: str):
    """
    Converts the decimal number to binary number

    :param decimal_number: a decimal number
    :type decimal_number: str
    :return: the number in binary numeral system
    """
    digits = list()
    helper = int(decimal_number)

    if helper == 0:
        return 0

    if helper < 0:
        messagebox.showerror(title='Error', message='Current version does not support negative number conversion!')
        return None

    while helper >= 1:
        helper_2 = helper % 2
        digits.append(str(0)) if helper_2 == 0 else digits.append(str(1))
        helper = helper // 2

    return ''.join(reversed(digits))


def is_binary_number_valid(number: str):
    """
    Function checks whether the binary number is valid (checks whether all digits are 0s and 1s)

    :param number: the binary number in string format
    :type number: str
    :return: True if the number is valid, False otherwise
    """
    digits = list()

    for char in number:
        digits.append(char)

    unique = list(set(digits))
    predicate = '2' in unique or '3' in unique or '4' in unique or '5' in unique or '6' in unique or '7' in unique or \
                '8' in unique or '9' in unique
    if (len(unique) == 2 or len(unique) == 1) and ('1' in unique or '0' in unique) and not predicate:
        return True
    else:
        return False


def button_convert_click():
    selected = var.get()
    text_1 = text_box_1.get('1.0', 'end-1c')
    text_2 = text_box_2.get('1.0', 'end-1c')

    if text_1 == '' and text_2 == '':
        messagebox.showerror(title='Error', message='Enter either a binary number or a decimal number!')
        return None

    if selected == '':
        messagebox.showerror(title='Error', message='No numeral system is selected!')
        return None
    elif selected == 'binary':
        text_box_1.delete(1.0, END)
        if text_2 == '':
            messagebox.showerror(title='Error', message='Decimal Number field is empty!')
            return None
        else:
            try:
                num = int(text_2)
            except ValueError:
                messagebox.showerror(title='Error', message='Decimal Number contains invalid input!')
                return None
            result = convert_decimal_to_binary(str(num))
            if result is None:
                return None
            text_box_1.insert(index=END, chars=result)
    else:
        text_box_2.delete(1.0, END)
        if text_1 == '':
            messagebox.showerror(title='Error', message='Binary Number field is empty!')
            return None
        else:
            try:
                num = int(text_1)
                if is_binary_number_valid(str(num)) is False:
                    raise ValueError
            except ValueError:
                messagebox.showerror(title='Error', message='Binary Number contains invalid input!')
                return None
            result = convert_binary_to_decimal(str(num))
            if result is None:
                return None
            text_box_2.insert(index=END, chars=result)

    return None


if __name__ == '__main__':
    form = Tk()
    form.wm_title('Binary/Decimal Converter')
    form.geometry('480x220')

    label_1 = Label(master=form, text='Binary Number')
    label_1.pack()

    text_box_1 = Text(master=form, height=1, width=400)
    text_box_1.pack()

    label_2 = Label(master=form, text='Decimal Number')
    label_2.pack(pady=(20, 0))

    text_box_2 = Text(master=form, height=1, width=400)
    text_box_2.pack()

    button = Button(master=form, height=1, width=10, text='Convert', command=button_convert_click)
    button.pack(pady=(20, 0))

    label_3 = Label(master=form, text='Converting to:')
    label_3.pack(padx=(180, 0), pady=(20, 0), side=LEFT)

    li = ['binary', 'decimal']
    var = StringVar()
    var.set('')
    drop_down_list = OptionMenu(form, var, *li)
    drop_down_list.config(width=80)
    drop_down_list.pack(padx=(0, 100), pady=(20, 0), side=RIGHT)

    form.mainloop()
