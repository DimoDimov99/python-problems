from utils.test_program_output import test_output


def josephus(number_of_people, start):
    index = 0
    circle = [x for x in range(1, number_of_people + 1)]
    print(circle)
    if len(circle) == 1:
        return circle[0]
    while len(circle) > 1:
        # start - 1 is the actually position; EG; start=2 item is at index[2 - 1]
        index = (index + (start - 1)) % len(circle)
        circle.pop(index)
    return circle[0]


test_data = [
    ([5, 2], 3),
    ([7, 3], 4),
    ([1, 1], 1),
]

if __name__ == "__main__":
    test_output(test_data, josephus, True, 2)
