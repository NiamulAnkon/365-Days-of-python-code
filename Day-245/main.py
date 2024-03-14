def linear_search(num_list, num_to_find):
    for index, element in enumerate(num_list):
        if element == num_to_find:
            return index
    return -1

def Binary_search(num_list, num_to_find):
    left_index = 0
    right_index = len(num_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_num = num_list[mid_index]

        if mid_num == num_to_find:
            return mid_index
        if mid_num < num_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)



if __name__ == "__main__":
    num_list = [12, 15, 17, 19, 21, 24, 45, 67]
    num_to_find = 15

    # index = linear_search(num_list, num_to_find)
    index = binary_search_recursive(num_list, num_to_find, 0, len(num_list))

    print(index)
