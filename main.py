def print_hello_name(name):
    print(f'Hello, {name}!')


def main():
    # print(repr(__name__))
    print("Hello World!")
    print("What is your name?")
    name = input()
    print_hello_name(name)


if __name__ == '__main__':
    main()
