class exc_10:
    def __init__(self):
        self.sorted_list = []


    def insertion_sort(self ,elements):
        self.sorted_list.append(elements)
        self.sorted_list.sort()
        # for i in range(1, len(elements)):
        #     anchor = elements[i]
        #     j =  i - 1
        #     while j>= 0 and anchor < elements[j]:
        #         elements[j+1] = elements[j]
        #         j = j - 1
        #     elements[j+1] = anchor

    def get_median(self):
        n = len(self.sorted_list)
        if n % 2 == 0:
            mid = n // 2
            return (self.sorted_list[mid - 1] + self.sorted_list[mid]) / 2
        else:
            return self.sorted_list[n // 2]

if __name__ == "__main__":
    stream = [2, 1, 5, 7, 2, 0, 5]
    root = exc_10()

    for element in stream:
        root.insertion_sort(element)
        print(root.get_median())