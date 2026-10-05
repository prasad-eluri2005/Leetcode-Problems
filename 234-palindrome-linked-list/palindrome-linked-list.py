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
        res1 = res[::-1]
        return (res[:cnt//2] == res1[:cnt//2])
        

        print(cnt)