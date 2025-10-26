class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bucket = [0] * (len(nums) + 1)
        for num in nums:
            bucket[num] = 1
        for i in range(len(bucket)):
            if bucket[i] == 0:
                return i
        