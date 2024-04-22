# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        right_view = []
        queue = [root]
        
        while queue:
            # Number of elements in the current level
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)
                
                # Capture the last element of each level
                if i == level_length - 1:
                    right_view.append(node.val)
                
                # Add left and right children of the node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_view