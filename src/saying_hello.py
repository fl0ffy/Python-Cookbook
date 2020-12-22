# 01 Saying Hello
#     create a program that prompts for your name and prints a greeting using your name.
# Example Output
# ​ 	What is your name? Brian
# ​ 	Hello, Brian, nice to meet you!
# Constraint
#     Keep the input, string concatenation, and output separate.
# Challenges
#
#     Write a new version of the program without using any variables.
#
#     Write a version of the program that displays different greetings for different people.
#     This would be a good challenge to try after you’ve completed the exercises in Chapter 4,
#     ​Making Decisions​ and Chapter 7, ​Data Structures​.


def get_input() -> str:
    return input("What is your name?\n")


def generate_greeting(name: str) -> str:
    return f'Hello, {name}, nice to meet you!'


def output(s: str) -> None:
    print(s)
    return


def saying_hello() -> None:
    output(generate_greeting(get_input()))


if __name__ == '__main__':
    saying_hello()
