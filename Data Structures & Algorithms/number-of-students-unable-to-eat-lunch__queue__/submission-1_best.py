from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res=len(sandwiches)
        tracker=Counter(students)
        
        for s in sandwiches:
            if tracker[s] > 0:
                res -=1
                tracker[s]-=1
            else:
                return res
        
        return res