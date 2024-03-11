class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def is_palindrome(s):
            return s == s[::-1]

        word_map = {word[::-1]: i for i, word in enumerate(words)}
        print(word_map)
        result = set()

        for i, word in enumerate(words):

            if "" in word_map and word != "" and is_palindrome(word):
                result.add((i, word_map[""]))
                result.add((word_map[""], i))

            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                
                if is_palindrome(prefix) and suffix in word_map and i != word_map[suffix]:
                    result.add((word_map[suffix], i))
                
                if j != 0 and is_palindrome(suffix) and prefix in word_map and i != word_map[prefix]:
                    result.add((i, word_map[prefix]))
                    
        return [list(pair) for pair in result]