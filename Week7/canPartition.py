class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        dp = [False] * (target + 1)
        dp[0] = True  # Zero sum is always possible, with the empty subset


        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True

        return dp[target]
