class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        i=0
        # nums1 has to be updated in place. object must remain the same
        # Use slice assignemnt nums1[:] to replace the entire contents of the original list object with the new elements
        # EFFETCS: truncates the list nums1 in place so that it only keeps its first m elements."
        nums1[:]=nums1[:m]

        while i<len(nums1) and j<n:
            if nums1[i]>nums2[j]:
                nums1.insert(i, nums2[j])
                j+=1
            i+=1
        nums1.extend(nums2[j:])

        # Potentially worst that all other submissions
        # We may need to shift all items in nums1 to the right using insert
        # for as many items as nums2 contains