# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        storage  = [head.val]
        run = head.next
        
        while run:
            storage.append(run.val)
            run = run.next
        
        storage_r = [storage[len(storage)-i-1] for i in range(len(storage)//2)]
        
        if storage[:len(storage)//2] == storage_r:
            return True
        else:
            return False