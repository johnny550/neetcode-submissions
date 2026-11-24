class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # x: append, push
        # +: append sum(score[-1]+score[i])
        # D: append 2 * score[-1]
        # C: pop
        tab=[]
        finalScore=0

        for op in operations:
            if op == "+":
                tab.append(tab[-1]+tab[-2])
            elif op == "D":
                tab.append(2 * tab[-1])
            elif op == "C":
                tab.pop()
            else:
                tab.append(int(op))


        return sum(tab)
