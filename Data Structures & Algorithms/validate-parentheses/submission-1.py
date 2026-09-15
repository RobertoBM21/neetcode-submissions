class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for val in s:
            if val not in closeToOpen:
                stack.append(val)
            else:
                if stack and stack[-1] == closeToOpen[val]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False