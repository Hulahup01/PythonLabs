import os
import re
import pickle


class Container:

    SAVE_PATH = os.path.relpath("data/")

    def __init__(self):
        self.__data = set()

    @property
    def data(self):
        """ Getter of __data """
        return self.__data

    @data.setter
    def data(self, new_data: set):
        """ Setter  of __data """
        self.__data = new_data

    def add(self, *keys: tuple):
        """ Adds new key(s) to the storage """
        self.data.update(keys)
        
    def remove(self, key):
        """ Removes key from the storage """
        self.data.discard(key)

    def find(self, *keys: tuple):
        """ Returns key(s) if key(s) is present in the storage """
        return [key for key in keys if key in self.data]
    
    def list(self):
        """ Returns list of elements """
        return list(self.data)
    
    def grep(self, regex: str):
        """ Uses regular expressions to find elements in storage """
        try:
            return [element 
                    for element in self.data
                      if re.findall(regex, element)]
        except re.error:
            return []
    
    def save(self, source: str):
        """ Saves data to the file with the given path """
        path = os.path.join(self.SAVE_PATH, f"{source}.pkl")

        with open(path, 'wb+') as save_file:
            pickle.dump(self.data, save_file)

    def load(self, source: str, switch=False):
        """ Loads data to storage from container with the given path """
        path = os.path.join(self.SAVE_PATH, f"{source}.pkl")

        if not os.path.lexists(path):
            if switch:
                self.data = set()
            return

        with open(path, 'rb') as load_file:
            try:
                new_data: set = pickle.load(load_file)
            except pickle.UnpicklingError:
                new_data = set()

        if switch:
            self.data = new_data
        else:
            self.data.update(new_data)  
