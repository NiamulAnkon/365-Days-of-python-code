def is_palindrome(s: str) -> bool:
    s = "".join(char.lower() for char in s if char.isalnum())

    left, right = 0, len(s) -1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right += 1
        return True
# Test cases
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("A man, a plan, a canal, Panama!"))  # Output: True
print(is_palindrome("python"))  # Output: False