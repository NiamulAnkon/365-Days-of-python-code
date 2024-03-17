def bubble_sort(element, key=None):
    size = len(element)

    for k in range(size - 1):
        swaped = False
        for i in range(size-1-k):
            a = element[i][key]
            b = element[i + 1][key]

            if a > b:
                tmp = element[i]
                element[i] = element[i + 1]
                element[i + 1] = tmp
                swaped = True

        if not swaped:
            break



if __name__ == "__main__":
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements, key='transaction_amount')
    # bubble_sort(elements, key='name')

    print(elements)
