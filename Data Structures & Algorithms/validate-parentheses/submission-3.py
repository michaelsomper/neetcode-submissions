class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_length = 0


        open_chars = set(['(', '{', '['])
        close_chars = set([')', '}', ']'])

        for char in s:
            if char in open_chars:
                stack.append(char)
                stack_length += 1
            else:
                if not stack:
                    return False
                if char == ')':
                    if stack[stack_length - 1] == '(':
                        stack.pop()
                        stack_length -= 1
                    else:
                        return False
                elif char == '}':
                    if stack[stack_length - 1] == '{':
                        stack.pop()
                        stack_length -= 1
                    else:
                        return False
                else:
                    if stack[stack_length - 1] == '[':
                        stack.pop()
                        stack_length -= 1
                    else:
                        return False
        if not stack:
            return True
        else:
            return False