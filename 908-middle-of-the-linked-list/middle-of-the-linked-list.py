# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        l = 0
        temp = head
        while temp != None:
            temp = temp.next
            l += 1
        mid = l//2
        temp = head
        while mid > 0:
            temp = temp.next
            mid -= 1
        return temp