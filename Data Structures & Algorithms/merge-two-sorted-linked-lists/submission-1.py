# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mHead = None
        oneNode = list1
        twoNode = list2
        if not oneNode and not twoNode:
            return mHead
        if not oneNode:
            mHead = twoNode
            twoNode = twoNode.next
        elif not twoNode:
            mHead = oneNode
            oneNode = oneNode.next
        elif oneNode.val < twoNode.val:
            mHead = oneNode
            oneNode = oneNode.next
        else:
            mHead = twoNode
            twoNode = twoNode.next
        mNode = mHead
        while oneNode or twoNode:
            if not oneNode:
                mNode.next = twoNode
                twoNode = twoNode.next
            elif not twoNode:
                mNode.next = oneNode
                oneNode = oneNode.next
            elif oneNode.val < twoNode.val:
                mNode.next = oneNode
                oneNode = oneNode.next
            else:
                mNode.next = twoNode
                twoNode = twoNode.next
            mNode = mNode.next
        return mHead
