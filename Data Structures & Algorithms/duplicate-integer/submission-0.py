class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set()
        for number in nums:
            if number in unique_numbers:
                return True
            else:
                unique_numbers.add(number)
        return False