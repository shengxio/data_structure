# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_head = ListNode()
        num_1 = l1
        num_2 = l2
        
        result = num_1.val + num_2.val
        l_head.val = result%10
        
        if num_1.next is None and num_2.next is None and result <10:
            return l_head
        else:
            l_head.next = ListNode(result//10)
            l_next = l_head.next
        
        
        while True:
            result = l_next.val
            if num_1.next:
                num_1 = num_1.next
                result += num_1.val
                
            if num_2.next:
                num_2 = num_2.next
                result += num_2.val
            l_next.val = result %10
            if num_1.next is None and num_2.next is None and result <10:
                return l_head
            else:
                l_next.next = ListNode(result//10)
                l_next = l_next.next
                        
        return l_head