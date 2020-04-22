# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        li = [head]
        while li[-1].next:
            li.append(li[-1].next)
        return(li[len(li) // 2])
