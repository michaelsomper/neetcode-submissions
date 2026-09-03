class Solution:
    def findMin(self, nums: List[int]) -> int:
        # So we have the midpoint
        # If the first number is bigger than the midpoint, it is in that half
        # If the last number is smaller than the midpoint, it is in that half

        while len(nums) > 3:
            mid = nums[len(nums) // 2]
            if nums[0] > mid:
                nums = nums[0:len(nums) // 2 + 1]
            elif nums[-1] < mid:
                nums = nums[len(nums) // 2: len(nums)]
            else:
                return nums[0]

        min_num = 1001
        for num in nums:
            if num < min_num:
                min_num = num
        return min_num
