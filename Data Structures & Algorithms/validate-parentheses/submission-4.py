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
                # find l's match in hashmap
                l_match=matches[l]
                # is match the same char as the one at the top of stack
                if stack and l_match==stack[-1]:
                    # yes
                    print(f"popping {stack[-1]}")
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return not stack