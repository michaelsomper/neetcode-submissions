class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_min = 0
        index_max = len(numbers) - 1

        sum_nums = numbers[index_min] + numbers[index_max]
        while sum_nums != target:
            if sum_nums < target:
                index_min += 1
            if sum_nums > target:
                index_max -= 1
            sum_nums = numbers[index_min] + numbers[index_max]

        return [index_min + 1, index_max + 1]


