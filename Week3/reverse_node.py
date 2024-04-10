# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 1:
            return head
    
        # First, determine the length of the linked list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        # Dummy node initialization
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        # Process every group of k nodes
        while length >= k:
            current = prev_group_end.next
            next_group_start = current.next
            
            # Reverse k nodes
            for i in range(1, k):
                next_node = next_group_start.next
                next_group_start.next = current
                current = next_group_start
                next_group_start = next_node
            
            # Connect with the previous part
            tail = prev_group_end.next
            tail.next = next_group_start
            prev_group_end.next = current
            prev_group_end = tail
            
            length -= k
        
        return dummy.next