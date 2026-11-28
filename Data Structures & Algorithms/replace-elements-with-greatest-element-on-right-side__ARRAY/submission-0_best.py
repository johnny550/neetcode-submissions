class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        j=1
        for i,val in enumerate(arr):
            j=i+1
            newMax=-1
            while j <len(arr):
                newMax=max(newMax,arr[j])
                j+=1
            arr[i]=newMax
        return arr