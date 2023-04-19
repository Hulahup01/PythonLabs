CONSOLE_COMMANDS = {
    "add": "add element1, element2",
    "remove": "remove element",
    "find": "find element1, element2",
    "list": "list all elements",
    "grep": "grep Regex",
    "save": "save container to the file",
    "load": "load container from the file",
    "switch": "switch USER_NAME",
    "exit": "exit the console"
}

LOAD_PROMPT = "Load {}'s data? [y][n]: "
SAVE_PROMPT = "Save {}'s data before switching? [y][n]: "
EXIT_PROMPT = "Save {}'s data before exiting? [y][n]: "

CONSOLE_HELP = "\n-==All commands==-\n"
for command, description in CONSOLE_COMMANDS.items():
    CONSOLE_HELP += f"- {command}: {description}\n"
CONSOLE_HELP += "--===============--\n"
