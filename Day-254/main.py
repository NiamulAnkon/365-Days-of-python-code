def multilevel_selection_sort(elements, sort_by_list):
    size = len(elements)
    for sort_by in sort_by_list[-1::-1]:
        for x in range(len(elements)):
            min_index = x
            for y in range(x, len(elements)):
                if elements[y][sort_by] < elements[min_index][sort_by]:
                    min_index = y
            if x != min_index:
                elements[x], elements[min_index] = elements[min_index], elements[x]
                           
if __name__ == "__main__":
    elements = [
        {'First Name': 'Raj'},
        {'First Name': 'Suraj'},
        {'First Name': 'Karan'},
        {'First Name': 'Jade'},
        {'First Name': 'Raj'},
        {'First Name': 'Raj'},
        {'First Name': 'Kiran'},
        {'First Name': 'Armaan'},
        {'First Name': 'Jaya'},
        {'First Name': 'Ingrid'},
        {'First Name': 'Jaya'},
        {'First Name': 'Armaan'},
        {'First Name': 'Ingrid'},
        {'First Name': 'Aahana'}
        ]
    multilevel_selection_sort(
        elements, ['First Name'])
    print(f'Array after Multi-Level Sorting:', *elements, sep='\n')