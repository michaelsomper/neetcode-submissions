# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Start with second index
        if len(pairs) == 0:
            return []
        transitions = []
        transitions.append(pairs[:])
        for i in range(1, len(pairs)):
            pair = pairs[i]
            key = pair.key

            pointer = i - 1
            while True:
                if pairs[pointer].key > key:
                    pairs[pointer + 1] = pairs[pointer]
                    pointer -= 1
                    if pointer < 0:
                        break
                else:
                    break

            pairs[pointer + 1] = pair
            transitions.append(pairs[:])

        return transitions

            


