# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  
        output_list=ListNode()
        tail=output_list
        while list1 and list2:
            # output_list.next=min(head_l1.next,head_l2.next)
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        
        if not list2:
            tail.next=list1
        if not list1:
            tail.next=list2

        return output_list.next
            