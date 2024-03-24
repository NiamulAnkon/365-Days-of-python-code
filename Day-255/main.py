def two_sum(nums, target):
    num_indices = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_indices:
            return [num_indices[complement], i]
        
        num_indices[num] = i
    
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    output = two_sum(nums, target)
    print("Output:", output)
