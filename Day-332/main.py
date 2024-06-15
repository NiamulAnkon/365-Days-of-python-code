def find_duplicates(list):
    _size_of_list = len(list)
    repeated = []
    for i in range(_size_of_list):
        k = i + 1
        for j in range(k, _size_of_list):
            if list[i] == list[j] and list[i] not in repeated:
                repeated.append(list[i])
    return repeated


list_of_int = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(find_duplicates(list_of_int))
