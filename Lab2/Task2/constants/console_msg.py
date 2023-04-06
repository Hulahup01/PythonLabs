CONSOLE_COMMANDS = {
    "add": "add elements to the container",
    "remove": "remove element from the container",
    "find": "find element in the container",
    "list": "list all elements of the container",
    "grep": "check if element suitable for provided regEx  is present in the container",
    "save": "save container to the file",
    "load": "load container from the file",
    "switch": "switch to another user",
    "exit": "exit the console"
}

LOAD_PROMPT = "Load {}'s data? [y][n]: "
SAVE_PROMPT = "Save {}'s data before switching? [y][n]: "
EXIT_PROMPT = "Save {}'s data before exiting? [y][n]: "

CONSOLE_HELP = "\n-==All commands==-\n"
for command, description in CONSOLE_COMMANDS.items():
    CONSOLE_HELP += f"{command}: {description}\n"
CONSOLE_HELP += "--===============--\n"