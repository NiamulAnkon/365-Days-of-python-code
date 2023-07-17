#Problem:
#Write a Python program that takes a list of numbers as input and returns the largest and smallest numbers from the list.

def find_max_min(numbers):
        if not numbers:
            return None, None
            
        min_number = max_num = numbers[0]
        for num in numbers:
            if(num < min_number):
                min_number  = num
            if(num > max_num):
                max_num = num

        return min_number, max_num


    #Example usage
numbers = [4,1,8,9,0,1,3,5]
min_val, max_val = find_max_min(numbers)
print(f"Minimum numbers is: {min_val}")
print(f"Maximum number is: {max_val}")
