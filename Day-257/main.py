def length_of_longest_substring(s):
    max_length = 0
    start = 0
    char_indices = {}
    
    for i, char in enumerate(s):
        if char in char_indices and char_indices[char] >= start:
            start = char_indices[char] + 1
        char_indices[char] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length


if __name__ == "__main__":
    s = "abcabcbb"
    output = length_of_longest_substring(s)
    print("Output:", output)
