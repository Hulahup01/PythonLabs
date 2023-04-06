from .container import Container

class User:

    def __init__(self, username: str):
        self._username = username
        self._container = Container()

    @property
    def username(self):
        """ Getter of _username """
        return self._username

    @username.setter
    def username(self, new_username: str):
        """ Setter of _username """
        self._username = new_username

    @property
    def container(self):
        """ Getter of _container """
        return self._container

    def add_keys(self, *keys: tuple):
        """ Adds keys to container """
        self.container.add(*keys)

    def remove_key(self, key):
        """ Removes a key from container """
        self.container.remove(key)

    def find_keys(self, keys: tuple):
        """ Prints the result of Container find method """
        found = self.container.find(*keys)
        print(f"Result(find()): {found if found else 'empty'}")

    def list_keys(self):
        """Prints data in list """
        print(f"Result(list()): {self.container.list()}")

    def grep_keys(self, regex: str):
        """ Prints the result of Conatainer grep method """
        print(f"Result(grep(): {self.container.grep(regex)}")

    def save_data(self):
        """ Saves data to the file with user's name as a filename """
        self.container.save(self.username)

    def load_data(self):
        """ Loads data from the file with user's name as a filename """
        self.container.load(self.username)

    def switch(self):
        pass