class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_value = amount + 1
        dp = [max_value] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make the amount 0

        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != max_value else -1