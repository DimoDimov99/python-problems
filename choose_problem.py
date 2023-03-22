import os
import sys
import random

WORKING_DIR = os.getcwd()


def clear():
    os.system("clear")


def get_all_available_problems():
    os.chdir(f"{WORKING_DIR}/problems_desc")
    txt_files = []
    for x in os.listdir():
        if x.endswith(".txt"):
            txt_files.append(x)

    return txt_files


def get_random_problem_to_solve():
    all_available_problems = get_all_available_problems()

    random_problem = random.choice(all_available_problems)

    with open(random_problem, "rt", encoding="utf8") as file:
        for line in file:
            print(line.strip())


def get_all_problems_without_extension():
    all_available_problems = get_all_available_problems()
    all_problems_names_without_extension = []
    for problem in all_available_problems:
        all_problems_names_without_extension.append(
            problem.replace(".txt", ""))

    return all_problems_names_without_extension


def show_problem_solution():
    all_problems_names_without_extension = get_all_problems_without_extension()

    print("All available problems:")
    for problem in all_problems_names_without_extension:
        print(problem)

    choice = input("Choose for which problem you want to see the solution: ")
    if choice in all_problems_names_without_extension:
        os.chdir(f"{WORKING_DIR}/problem_solutions")
        try:
            with open(f"{choice}.txt", "rt", encoding="utf8") as file:
                clear()
                for line in file:
                    print(line.rstrip('\n'))  # handle whitespaces
        except FileNotFoundError:
            sys.exit("TBD")


options = {
    "problem": get_random_problem_to_solve,
    "solution": show_problem_solution
}


def main(arg):
    clear()
    try:
        return options[arg]()
    except KeyError:
        print("Invalid input")
        return -1


if __name__ == "__main__":
    user_input = input(
        "Type 'problem' to get random problem to solve. Type 'solution' to see problem solution. Type 'quit' to quit\n")
    while user_input != 'quit':
        main(user_input)
        user_input = input(
            "Type 'problem' for random problem to solve or type 'solution' to see problem solution. Type 'quit' to quit\n")
    print("Quiting...")
