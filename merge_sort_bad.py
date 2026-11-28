class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # merge the two arrays
        i,j = 0,0
        while j<len(nums2) and i<len(nums1):
            print(i,j)
            print(nums1[i],nums2[j])
            if nums2[j] < nums1[i] or nums1[i] == 0:
                templast=nums1[len(nums1)-1]
                tempk=nums1[i]

                nums1[i] = nums2[j]
                nums1[len(nums1)-2] = templast
                nums1[len(nums1)-1] = tempk
                j+=1
                print(nums1)
            else:
                i+=1

        # sort the merged array using mergeSort
        print(f"merging both in one returns: {nums1}")
        return self.mergeSort(nums1,0,len(nums1)-1)

    def mergeSort(self, arr,s,e):
        # print(f"sorting {arr}")
        # s,e=0,len(arr)-1
        if e-s+1 <= 1:
            return arr

        m=(s+e) // 2

        # mergeSort left hand side
        self.mergeSort(arr, s,m)

        # mergeSort right hand side
        self.mergeSort(arr, m+1, e)

        self.mergeArr(arr,s,m,e)

        return arr

    def mergeArr(self, arr, s, m, e):
        l_arr = arr[s:m+1]
        r_arr = arr[m+1:e+1]
        i,j=0,0
        k=s

        while i<len(l_arr) and j<len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i+=1
            else:
                arr[k] = r_arr[j]
                j+=1
            k+=1

        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1
        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1

        
sol=Solution()

# nums1 = [10,20,20,40,0,0]
# m = 4
# nums2 = [1,2]
# n = 2

nums1=[0,0]
m=0
nums2=[1,2]
n=2

print(f"sorted merged array is: {sol.merge(nums1,m,nums2,n)}")