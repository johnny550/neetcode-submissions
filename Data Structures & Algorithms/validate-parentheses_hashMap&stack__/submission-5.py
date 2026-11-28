from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # Every open bracket is closed by the same type of close bracket.
        # Open brackets are closed in the correct order.
        # Every close bracket has a corresponding open bracket of the same type.
        matches={"}":"{", "]":"[", ")":"("}
        stack=deque()
        for l in s:
            if l in matches: 
                # is l's match the same char as the one at the top of stack
                if stack and matches[l]==stack[-1]:
                    # yes
                    print(f"popping {stack[-1]}")
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return not stack