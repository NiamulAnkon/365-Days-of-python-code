class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

if __name__ == "__main__":
    num1 = [1,1,2]
    sltn = Solution()
    sltn.removeDuplicates(num1)
