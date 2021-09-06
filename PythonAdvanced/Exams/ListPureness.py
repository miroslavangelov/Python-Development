from collections import deque


def best_list_pureness(list_of_numbers, k):
    best_sum = 0
    best_rotation = 0
    queue = deque(list_of_numbers)

    for i in range(0, k + 1):
        current_sum = 0
        for j in range(0, len(queue)):
            current_number = queue[j]
            current_sum += j * current_number

        # change numbers positions
        queue.rotate(1)

        if current_sum > best_sum:
            best_sum = current_sum
            best_rotation = i

    return f'Best pureness {best_sum} after {best_rotation} rotations'


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
