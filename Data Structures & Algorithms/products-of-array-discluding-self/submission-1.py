class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [nums[0]]
        suffix_products = [nums[len(nums) - 1]]

        for i in range(1, len(nums)):
            prefix_products.append(prefix_products[i - 1] * nums[i])
            suffix_products.append(suffix_products[i - 1] * nums[len(nums) - 1 - i])

        # print(prefix_products)
        # print(suffix_products)

        except_self = []

        for i in range(len(nums)):
            if i == 0:
                except_self.append(suffix_products[len(nums) - 2])
            elif i == len(nums) - 1:
                except_self.append(prefix_products[len(nums) - 2])
            else:
                answer = prefix_products[i - 1] * suffix_products[len(nums) - 2 - i]
                except_self.append(answer)

        return except_self