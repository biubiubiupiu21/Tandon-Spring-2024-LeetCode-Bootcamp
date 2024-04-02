class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        people = [0] * (n + 1)
        people[1] = 1  # On day 1, one person knows the secret
        
        for day in range(1, n + 1):
            # Share the secret: From day + delay to day + forget - 1, as they forget on day + forget
            for share_day in range(day + delay, min(day + forget, n + 1)):
                people[share_day] = (people[share_day] + people[day]) % MOD
        
        # Calculate how many people know the secret on day n
        total = sum(people[-forget:]) % MOD  # Only those who haven't forgotten know the secret
        
        return total