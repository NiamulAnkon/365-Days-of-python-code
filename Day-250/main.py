def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(element, start, end):
    pivot_index = start
    pivot = element[pivot_index]

    while start <= end:
        while start < len(element) and element[start] <= pivot:
            start += 1
        while element[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, element)
            start += 1
            end -= 1

    swap(pivot_index, end, element)
    return end

def quick_sort(element, start, end):
    if start < end:
        pi = partition(element, start, end)
        quick_sort(element, start, pi - 1)
        quick_sort(element, pi + 1, end)

if __name__ == "__main__":
    test = [ 
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
    ]

    for elements in test: 
        quick_sort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')