# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        kth = [10**6+1]*k
        stack = []
        current = root
        
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if (current.val <= max(kth)):
                    kth[kth.index(max(kth))] = current.val
                current = current.right

        print(kth)
        return(kth[k-1])