class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsAppears = {}

        for i in nums:
            if i not in numsAppears:
                numsAppears[i] = 1
            else:
                return True
        
        return False