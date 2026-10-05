# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        cnt = 0
        temp = head
        res = []
        while temp != None:
            res.append(temp.val)
            temp = temp.next
            cnt += 1
        i = 0
        j = len(res)-1
        while i < j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        return True