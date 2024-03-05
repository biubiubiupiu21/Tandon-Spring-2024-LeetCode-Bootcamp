class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        n = len(clips) 
        clips.sort(key=lambda x: (x[0], -x[1]))  # Sort by start time, then by -end time
        print(clips)
        end, nextEnd, count, i = 0, 0, 0, 0

        while i < n and clips[i][0] <= end:
            # Look for the clip with the farthest end within clips that start not after 'end'
            while i < n and clips[i][0] <= end:
                nextEnd = max(nextEnd, clips[i][1])
                i += 1
            count += 1  # Include this clip
            end = nextEnd  # Extend the coverage

            if end >= time:  # Check if we've covered the required time
                return count
        
        return -1