import os
import re
from datetime import datetime


class Contact:
    """
    A class for creating contacts. Contacts contain the following information: name, surname, phone, email and date and
    time when the contact was added.
    """

    def __init__(self, *args, **kwargs):
        """
        The constructor for the Contact class. Can be used with *args, **kwargs or a combination of both. Raises
        Exception and Errors where needed. Currently it does not validate user input
        (Method is complicated because I wanted to experiment with args and kwargs)

        :param args: arguments for the constructor in tuple format
        :param kwargs: arguments for the constructor in dictionary format
        :returns: None
        """
        if len(args) == 0 and not kwargs:
            raise Exception('Cannot create an empty contact!')
        elif len(args) == 0 and kwargs:
            try:
                self._name = kwargs['name']
                self._surname = kwargs['surname']
                self._phone = kwargs['phone']
                self._email = kwargs['email']
                self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                if self.validate_data() is False:
                    raise TypeError('Some or all of the data is not of str type. Constructor requests string data.')
            except KeyError:
                raise Exception('Not all data is given to the Contact constructor. '
                                'Constructor requests: name, surname, phone '
                                'and email. All data must be of str type. Also, incorrect keyword arguments may be '
                                'given.')
        elif len(args) != 0 and not kwargs:
            if len(args) < 4:
                raise Exception('Not all data is given to the Contact constructor. '
                                'Constructor requests: name, surname, phone '
                                'and email. All data must be of str type.')
            elif len(args) > 4:
                raise Exception('Too much data is given to the Contact constructor. '
                                'Constructor requests: name, surname, phone '
                                'and email. All data must be of str type.')
            else:
                self._name = args[0]
                self._surname = args[1]
                self._phone = args[2]
                self._email = args[3]
                self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                if self.validate_data() is False:
                    raise TypeError('Some or all of the data is not of str type. Constructor requests string data.')
        else:
            if len(kwargs.keys()) == 1:
                if 'name' in kwargs.keys():
                    self._name = kwargs['name']
                    if len(args) != 3:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._surname = args[0]
                        self._phone = args[1]
                        self._email = args[2]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'surname' in kwargs.keys():
                    self._surname = kwargs['surname']
                    if len(args) != 3:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._name = args[0]
                        self._phone = args[1]
                        self._email = args[2]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'phone' in kwargs.keys():
                    self._phone = kwargs['phone']
                    if len(args) != 3:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._name = args[0]
                        self._surname = args[1]
                        self._email = args[2]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'email' in kwargs.keys():
                    self._email = kwargs['email']
                    if len(args) != 3:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._name = args[0]
                        self._surname = args[1]
                        self._phone = args[2]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                else:
                    raise KeyError('Incorrect keyword argument is given')
            elif len(kwargs.keys()) == 2:
                if 'name' in kwargs.keys() and 'surname' in kwargs.keys():
                    self._name = kwargs['name']
                    self._surname = kwargs['surname']
                    if len(args) != 2:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._phone = args[0]
                        self._email = args[1]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'name' in kwargs.keys() and 'phone' in kwargs.keys():
                    self._name = kwargs['name']
                    self._phone = kwargs['phone']
                    if len(args) != 2:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._surname = args[0]
                        self._email = args[1]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'name' in kwargs.keys() and 'email' in kwargs.keys():
                    self._name = kwargs['name']
                    self._email = kwargs['email']
                    if len(args) != 2:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._surname = args[0]
                        self._phone = args[1]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'surname' in kwargs.keys() and 'phone' in kwargs.keys():
                    self._surname = kwargs['surname']
                    self._phone = kwargs['phone']
                    if len(args) != 2:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._name = args[0]
                        self._email = args[1]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'surname' in kwargs.keys() and 'email' in kwargs.keys():
                    self._surname = kwargs['surname']
                    self._email = kwargs['email']
                    if len(args) != 2:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._name = args[0]
                        self._phone = args[1]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'phone' in kwargs.keys() and 'email' in kwargs.keys():
                    self._phone = kwargs['phone']
                    self._email = kwargs['email']
                    if len(args) != 2:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._name = args[0]
                        self._surname = args[1]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                else:
                    raise RuntimeError('Constructor arguments error. Please check the given arguments')
            elif len(kwargs.keys()) == 3:
                if 'name' in kwargs.keys() and 'surname' in kwargs.keys() and 'phone' in kwargs.keys():
                    self._name = kwargs['name']
                    self._surname = kwargs['surname']
                    self._phone = kwargs['phone']
                    if len(args) != 1:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._email = args[0]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'name' in kwargs.keys() and 'surname' in kwargs.keys() and 'email' in kwargs.keys():
                    self._name = kwargs['name']
                    self._surname = kwargs['surname']
                    self._email = kwargs['email']
                    if len(args) != 1:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._phone = args[0]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'name' in kwargs.keys() and 'phone' in kwargs.keys() and 'email' in kwargs.keys():
                    self._name = kwargs['name']
                    self._phone = kwargs['phone']
                    self._email = kwargs['email']
                    if len(args) != 1:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._surname = args[0]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                elif 'surname' in kwargs.keys() and 'phone' in kwargs.keys() and 'email' in kwargs.keys():
                    self._surname = kwargs['surname']
                    self._phone = kwargs['phone']
                    self._email = kwargs['email']
                    if len(args) != 1:
                        raise Exception('Missing or too much data is given to the Contact constructor. Constructor '
                                        'requests: name, surname, phone and email. All data must be of str type.')
                    else:
                        self._name = args[0]
                        self._added_on = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                        if self.validate_data() is False:
                            raise TypeError('Some or all of the data is not of str type. Constructor requests string '
                                            'data.')
                else:
                    raise Exception('Constructor arguments error. Please check which arguments are passed')
            else:
                raise RuntimeError('Contact constructor error')

    def validate_data(self):
        """
        Checks whether all attributes are of type string

        :returns:
            - True if all object attributes are of type string
            - False otherwise
        """
        if type(self._name) is not str or type(self._surname) is not str or type(self._phone) is not str \
                or type(self._email) is not str:
            return False
        else:
            return True

    def get_contact_name(self):
        """
        Returns the contact's name

        :returns: the 'name' attribute of the calling Contact instance
        :rtype: str
        """
        return self._name

    def get_contact_surname(self):
        """
        Returns the contact's surname

        :returns: the 'surname' attribute of the calling Contact instance
        :rtype: str
        """
        return self._surname

    def get_contact_phone(self):
        """
        Returns the contact's phone number

        :returns: the 'phone' attribute of the calling Contact instance
        :rtype: str
        """
        return self._phone

    def get_contact_email(self):
        """
        Returns the contact's email

        :returns: the 'email' attribute of the calling Contact instance
        :rtype: str
        """
        return self._email

    def get_datetime_added(self):
        """
        Returns when the contact was added in the contact book

        :returns: the 'added_on' attribute of the calling Contact instance
        :rtype: str
        """
        return self._added_on

    def write_to_txt_file(self, file_path: str):
        """
        Writes the Contact object in the specified file. If the file does not exist, the method raises a
        FileNotFoundError

        :param file_path: absolute or relative file path to the file where the object should be written
        :type file_path: str
        :returns: None
        """
        s = self._name + ' ' + self._surname + '    ' + self._phone + '    ' + self._email + '    ' + self._added_on
        if os.path.isfile(file_path):
            with open(file_path, mode='a') as datafile:
                datafile.write(s + '\n')
            return None
        else:
            raise FileNotFoundError('File does not exist')

    def is_contact_email_valid(self):
        """
        Checks whether the contact's email address is valid using regex

        :returns:
            - True if the contact's email is a valid email address (valid by regex)
            - False otherwise
        """
        result = re.match(pattern=r'\w+\.?\w+\.?\w+@\w+\.com', string=self._email)
        if result is None:
            return False
        else:
            return True

    def is_contact_name_valid(self):
        """
        Checks whether the contact's name is valid. A valid name is a name that contains more than 3 characters

        :returns:
            - True if the contact's name is valid
            - False otherwise
        """
        result = re.match(pattern=r'\w{3,}', string=self._name)
        if result is None:
            return False
        else:
            return True

    def is_contact_phone_valid(self):
        """
        Checks whether the contact's phone number is valid. A valid phone number is of the format: +xxx xx xxx xxx

        :returns:
            - True if the contact's phone number is valid
            - False otherwise
        """
        result = re.match(pattern=r'^\+\d{3}\s\d{2}\s\d{3}\s\d{3}', string=self._phone)
        if result is None:
            return False
        else:
            return True

    def is_contact_surname_valid(self):
        """
        Checks whether the contact's surname is valid. A valid surname is a surname that contains at least 3 characters
        (Just like the name)

        :returns:
            - True if the contact's surname is valid
            - False otherwise
        """
        result = re.match(pattern=r'\w{3,}', string=self._surname)
        if result is None:
            return False
        else:
            return True

    def __str__(self):
        """
        Overrides the __str__ method for the Contact class

        :return s: a string representation of the Contact object
        :rtype: str
        """
        s = '------------------------------\n'
        s += 'Contact info:\n'
        s += f'Name: {self._name}\n'
        s += f'Surname: {self._surname}\n'
        s += f'Phone number: {self._phone}\n'
        s += f'Email: {self._email}\n'
        s += f'Added on: {self._added_on}\n'
        s += '------------------------------\n'
        return s

    def __eq__(self, other):
        """
        Overrides the __eq__ method for the Contact class

        :param other: an object to be tested for equality with the Contact instance that calls this method
        :type other: Any
        :returns:
            - True if self and other are the same object or have equal values for all attributes
            - False otherwise
        """
        if isinstance(other, Contact) is False:
            return False
        else:
            if self._name == other._name and self._surname == other._surname and self._phone == other._phone and \
                    self._email == other._email and self._added_on == other._added_on:
                return True
            else:
                return False


if __name__ == '__main__':
    c = Contact('Sample', 'Sample2', '111222333', email='test@test.com')
    c2 = Contact('Sample2', 'Sample3', '123456789', 'asdasd@dsas.com')
    c3 = Contact('a', 'bc', '+111 111 222', 'test')
    # print(c == c2)
    # c21 = Contact('1', '2', '3', '4', '5', '6')
    print(c3.is_contact_name_valid())
    print(c3.is_contact_phone_valid())
    print(c3.is_contact_email_valid())
    print(c3.is_contact_surname_valid())
