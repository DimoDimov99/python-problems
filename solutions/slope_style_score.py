from utils.test_program_output import test_output


def min_elem_index(arr):
    _min = arr[0]
    min_index = 0

    for elem in range(len(arr)):
        if arr[elem] < _min:
            _min = arr[elem]
            min_index = elem
    return min_index


def max_elem_index(arr):
    _max = arr[0]
    max_index = 0

    for elem in range(len(arr)):
        if arr[elem] > _max:
            _max = arr[elem]
            max_index = elem
    return max_index


def slope_style_score(scores):
    total_score = 0
    scores_after_removal = []
    scores_min_index = min_elem_index(scores)
    scores_max_index = max_elem_index(scores)

    for score in range(len(scores)):
        if score != scores_min_index and score != scores_max_index:
            scores_after_removal.append(scores[score])

    for score in scores_after_removal:
        total_score += score

    total_score = round(total_score / len(scores_after_removal), 2)

    return total_score


test_data = [
    ([94, 95, 95, 95, 90], 94.67),
    ([60, 70, 80, 90, 100], 80.0),
    ([96, 95.5, 93, 89, 92], 93.5)
]


if __name__ == "__main__":
    test_output(test_data, slope_style_score, True)
