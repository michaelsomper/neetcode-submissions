from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_dict = defaultdict(list)
        distinct_triplets = set()

        for i, num in enumerate(nums):
            nums_dict[num].append(i)

        print(nums_dict)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                two_sum = nums[i] + nums[j]
                if -two_sum in nums_dict:
                    if len(nums_dict[-two_sum]) > 1 or nums_dict[-two_sum][0] != i and nums_dict[-two_sum][0] != j:
                        if -two_sum == 0 and len(nums_dict[-two_sum]) < 3:
                            break
                        triplet = [nums[i], nums[j], -two_sum]
                        sorted_triplet = sorted(triplet)
                        sorted_triplet_tuple = tuple(sorted_triplet)
                        distinct_triplets.add(sorted_triplet_tuple)
        distinct_triplets_list = [list(tup) for tup in distinct_triplets]

        return distinct_triplets_list

                    




