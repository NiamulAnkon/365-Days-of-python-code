#Problem:
#Write a Python program that takes a list of numbers as input and returns a new list containing only the numbers that are divisible by 3 and 5.
try:
    def find_divisible_numbers(numbers):
        divisible_numbers = []
        for num in numbers:
            if num % 3 == 0 and num % 5 == 0:
                divisible_numbers.append(num)
        return divisible_numbers

    # Example usage
    numbers = [15, 10, 9, 12, 20, 30, 7]
    result = find_divisible_numbers(numbers)
    print(f"Divisible numbers:  {result}")
except Exception as e:
    print("Something Went wrong")