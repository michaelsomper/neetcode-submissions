class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        sorted_pairs = sorted(zip(position, speed))
        position, speed = map(list, zip(*sorted_pairs))

        stack.append((target - position[len(position) - 1]) / speed[len(position) - 1])

        for i in range(len(position) - 2, -1, -1):
            time = (target - position[i]) / speed[i]

            if stack[len(stack) - 1] < time:
                stack.append(time)

        return len(stack)

            
