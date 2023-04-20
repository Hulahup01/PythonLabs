from tools.statistics import get_statistics


def main():
    print("Enter the text: ")
    text = input()
    print(get_statistics(text))


def func(*args: tuple):
    print(args)

if __name__ == "__main__":
    main()


