import os
from contact import Contact


class ContactBook:
    """
    A class for creating a contact book which will contain multiple contacts.
    """
    def __init__(self, *args, **kwargs):
        """
        The constructor for the ContactBook class. It requires a list which contains elements of type Contact

        :param args: arguments for the constructor in tuple format
        :param kwargs: arguments for the constructor in dictionary format
        :returns: None
        """
        if len(args) == 0 and not kwargs:
            self._contacts = list()
        elif len(args) == 1 and not kwargs:
            arg = args[0]
            if ContactBook.check_data_type(arg) is False:
                raise Exception('Invalid data given to the ContactBook constructor. Constructor must take one argument'
                                'of type list which must contain elements of type Contact')
            else:
                self._contacts = arg
        elif len(args) == 0 and kwargs:
            try:
                if ContactBook.check_data_type(kwargs['contact']) is False:
                    raise Exception(
                        'Invalid data given to the ContactBook constructor. Constructor must take one argument'
                        'of type list which must contain elements of type Contact')
                else:
                    self._contacts = kwargs['contacts']
            except KeyError:
                raise Exception('Incorrect arguments to the ContactBook constructor or no data is given.')
        else:
            raise RuntimeError('ContactBook constructor error')

    def get_number_of_contacts(self):
        """
        Returns the number of contacts contained in the contact book

        :returns: the number of contacts in the instance
        """
        return len(self._contacts)

    def get_contacts(self):
        """
        Returns the list of contacts in the contact book

        :returns: the contacts in the contact book
        :rtype: list
        """
        return self._contacts

    def sort_contacts_by_key(self, key: str, flag: bool):
        """
        Sorts the contacts in the ContactBook instance by the given key

        :param key: the key by which the sorting should be done
        :type key: str
        :param flag: flag which tells us whether to sort the elements in ascending (False) or descending (True) order
        :type flag: bool
        :returns: None
        """
        assert key == 'name' or key == 'surname' or key == 'phone' or key == 'email'
        self._contacts.sort(key=lambda contact: contact.key, reversed=flag)

    def write_contacts_to_txt_file(self, file_path: str):
        """
        Writes all contacts in the contact book in the specified .txt file. Raises FileNotFoundError if the file does
        not exist

        :param file_path: absolute or relative path to the .txt file
        :type file_path: str
        :returns: None
        """
        if os.path.isfile(file_path):
            for c in self._contacts:
                c.write_to_txt_file(file_path)
            return None
        else:
            raise Exception('File does not exist')

    def read_contacts_from_txt_file(self, file_path: str):
        """
        Reads the contacts from the .txt file. Also, checks whether a string represents a contact
        (String must be the same as the way contacts are written in the file, not like the __str__() method of the
        Contact class)
        If file does not exist, raises a FileNotFoundException

        :returns: None
        """
        if os.path.isfile(file_path):
            with open(file_path, mode='r') as datafile:
                for line in datafile.readlines():
                    text = line.rstrip('\n').split(r'\s+')
                    try:
                        c = Contact(text[0], text[1], text[2], text[3])
                    except Exception or TypeError:
                        print('Invalid contact format. See Contact class\' write_to_file() method')
                    self._contacts.append(c)
        else:
            raise FileNotFoundError('File does not exist')

    @staticmethod
    def check_data_type(li: list):
        """
        Checks if a list is passed to the constructor and if all elements in the list are of type Contact

        :param li: a list containing objects
        :type li: list
        :returns:
            - True if a list is passed and all elements of that list are of type Contact
            - False otherwise
        """
        if isinstance(li, list):
            for el in li:
                if not isinstance(el, Contact):
                    return False
            return True
        else:
            return False

    def __str__(self):
        """
        Overrides the __str__() method for the contact book class

        :return s: string format of the ContactBook object
        :rtype: str
        """
        s = 'Printing all contacts from the contact book:\n'
        for c in self._contacts:
            s += str(c)
        s += '\n'

        return s


def clear_txt_file(file_path: str):
    """
    Clears the .txt file that contains the contacts. Raises a FileNotFoundError if file does not exist

    :param file_path: absolute or relative path to the datafile
    :returns: None
    """
    if os.path.isfile(file_path):
        with open(file_path, mode='w') as datafile:
            datafile.truncate()
    else:
        raise FileNotFoundError('The file does not exist')


if __name__ == '__main__':
    pass
