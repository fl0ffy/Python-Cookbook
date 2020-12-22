

def get_input() -> str:
    return input("What is your name?\n")


def generate_greeting(name: str) -> str:
    return f'Hello, {name}, nice to meet you!'


def  output(s: str) -> None:
    print(s)
    return


def saying_hello() -> None:
    name = get_input()
    output(generate_greeting(name))


if __name__ == '__main__':
    saying_hello()
