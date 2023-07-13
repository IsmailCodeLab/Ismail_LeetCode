# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size=0
        cur=head
        while cur:
            cur=cur.next
            size+=1
        index=size-n
        cur=head
        count=0
        if size==1 and n==1 or size==n:
            return head.next
        while count<index-1:
            cur=cur.next
            count+=1
        temp=cur.next
        cur.next=temp.next
        return head
            