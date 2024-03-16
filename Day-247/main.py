def bubble_sort(element):
    size = len(element)

    for k in range(size - 1):
        swaped = False
        for i in range(size-1 - k):
            if element[i] > element[i + 1]:
                tmp = element[i]
                element[i] = element[i + 1]
                element[i + 1] = tmp
                swaped = True
        if not swaped:
            break


if __name__ == "__main__":
    elements1 = [5,9,2,1,67,34,88,34]
    elements2 = [1,2,3,4]
    elements3 = ["a", "c", "t", "d", "z", "k", "b"]

    bubble_sort(elements1)
    bubble_sort(elements2)
    bubble_sort(elements3)
    
    print(f"Unsorted by default: {elements1}")
    print(f"Sorted by default {elements2}")
    print(f"String Sorted: {elements3}")
