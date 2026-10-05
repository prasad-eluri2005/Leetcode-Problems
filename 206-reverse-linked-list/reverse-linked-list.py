# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        res = []
        temp = head
        while temp != None:
            res.append(temp.val)
            temp = temp.next
        temp = head
        for i in range(len(res)-1,-1,-1):
            temp.val = res[i]
            temp = temp.next
        return head
