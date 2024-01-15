# Challenge 01
import random


class Student:
    education_platform = "Udemy"

    def __init__(self, name, age=18) -> None:
        self.name = name
        self.age = age

    def greet(self):
        greet_phrases = ["Hi, I'm", "Hey there, my name is", "Hi. Oh, my name is"]
        print(f"{random.choice(greet_phrases)} {self.name}")


def create_students_class_istances(students):
    students_list = []
    students_len = len(students)
    for i in range(students_len):
        students_list.append(Student(students[i]))
    return students_list


def create_students_class_istances2(students):
    return [Student(student) for student in students]


if __name__ == "__main__":
    students = ["Dimo", "Radina", "Aleks", "Bob", "Test", "Test", "Test3"]
    # First way
    """
    students_objects = create_students_class_istances(students)
    for obj in students_objects:
        obj.greet()
    """
    # Second way
    for student in create_students_class_istances2(students):
        student.greet()
