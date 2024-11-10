class MercedezBenz:
    def __init__(self, doors, wheels, model) -> None:
        self.doors = doors
        self.wheels = wheels
        self.model = model

    def drive(self):
        print(f"A car {self.model} is being driven")


class Student:
    def __init__(self, name, age, profile) -> None:
        self.name = name
        self.age = age
        self.profile = profile

    def print_student_info(self) -> None:
        print(f"Name: {self.name} | age: {self.age} | profile: {self.profile}")


if __name__ == "__main__":
    # ca1 = MercedezBenz(2, 4, "G-class")
    # ca1.drive()
    student01 = Student("Dimo", 24, "IT")
    student01.print_student_info()
