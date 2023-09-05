import os
import sys


def generate_boilerplate():
    current_directory = os.getcwd()
    filename = input("Filename: ").lower().strip()
    try:
        with open(f"{current_directory}/skeleton", "r", encoding="utf8") as file:
            lines = file.readlines()
        os.chdir(f"{current_directory}/solutions")
        # print(os.getcwd())
        with open(f"{filename}.py", "w", encoding="utf8") as file:
            for line in lines:
                file.write(line)
    except FileNotFoundError as e:
        sys.exit(e)


if __name__ == "__main__":
    generate_boilerplate()
