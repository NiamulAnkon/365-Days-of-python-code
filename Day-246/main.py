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
        mid_number = num_list[mid_index]

        if mid_number == num_to_find:
            return mid_index

        if mid_number < num_to_find: 
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

     return -1


def binary_search_recursive(num_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(num_list) or mid_index < 0:
        return -1

    mid_number = num_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(num_list, number_to_find, left_index, right_index)

def find_all_occurances(numbers, number_to_find):
    index = Binary_search(numbers, number_to_find)
    indices = [index]
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)



if __name__ == "__main__":
    num_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    num_to_find = 15

    index = find_all_occurances(num_list, num_to_find)

    print(index)