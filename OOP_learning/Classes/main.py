class MercedezBenz:
    def __init__(self, doors, wheels, model) -> None:
        self.doors = doors
        self.wheels = wheels
        self.model = model

    def drive(self):
        print(f"A car {self.model} is being driven")


if __name__ == "__main__":
    ca1 = MercedezBenz(2, 4, "G-class")
    ca1.drive()
