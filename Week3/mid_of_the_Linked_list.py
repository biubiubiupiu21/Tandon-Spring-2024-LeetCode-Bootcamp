class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        mid = 0
        temp = head
        midtemp = head

        while temp:
            count += 1
            if count%2 == 0:
                mid += 1
                midtemp = midtemp.next
            temp = temp.next

        return midtemp