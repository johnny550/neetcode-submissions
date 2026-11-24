class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # reverse iteration
        # maxVal=max(oldmax, arr[i])
        # initial max= -1

        rightMax=-1
        prev=0
        for i in range(len(arr)-1, -1, -1):
            newMax=max(rightMax, arr[i])
            arr[i]=rightMax
            rightMax=newMax

        return arr