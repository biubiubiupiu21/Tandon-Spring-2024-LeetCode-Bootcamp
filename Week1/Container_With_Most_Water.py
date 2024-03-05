class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        max_area = 0

        while start < end:
            width = end - start
            max_area = max(max_area, min(height[start], height[end]) * width)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area