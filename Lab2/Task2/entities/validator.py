import re

from constants.console_msg import CONSOLE_COMMANDS


class Validator:

    @classmethod
    def validate_command(cls, input_line: str):
        """ Check if the command is in input string """
        try:
            possible_command = input_line.split()[0]
        except IndexError:
            return "Not a command"

        if possible_command in CONSOLE_COMMANDS.keys():
            return possible_command
        else:
            return f"{possible_command}: command not found"

    @classmethod
    def get_username(cls):
        """ Get username from input string """
        while True:
            username = input("Enter your username: ")
            pattern = re.compile(r'^[a-zA-Z0-9]{3,}$')

            if bool(pattern.match(username)):
                return username
            else:
                print("Username must be at least 3 characters"
                      " long and contain only numbers and/or latin letters")

    @classmethod
    def validate_username(cls, username: str):
        username = username.strip()

        match = re.match(r'^[a-zA-Z0-9]{3,}$', username)
        if match is not None and username == match.group(0):
            return True
        else:
            return False

    @classmethod
    def validate_args(cls, input_line: str, grep: bool = False):
        """ Get args from input string """
        possible_args = input_line.split(maxsplit=1)

        if len(possible_args) < 2:
            return tuple()

        if grep:
            return tuple(possible_args[1])

        args = possible_args[1].split(',')

        for i in range(len(args)):
            args[i] = args[i].strip()

        args[:] = (value for value in args if value != "")

        return tuple(args)

    @classmethod
    def get_choice(cls, prompt):
        while True:
            choice = input(prompt)
            if choice == 'n' or choice == 'y':
                return choice