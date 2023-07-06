def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main():
    print(is_prime(2))
    print(is_prime(10))
    print(is_prime(17))


if __name__ == "__main__":
    main()
