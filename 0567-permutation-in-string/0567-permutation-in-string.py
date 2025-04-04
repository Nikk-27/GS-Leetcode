class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
# Sliding window approach

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        n = len(s1)
        m = len(s2)

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1


        if n > m:
            return False

        i = 0
        j = 0

        while j < m:
            s2_freq[ord(s2[j]) - ord('a')] += 1

            if (j - i + 1 > n):
                s2_freq[ord(s2[i]) - ord('a')] -= 1
                i += 1
            
            if s2_freq == s1_freq:
                return True
            
            j += 1
        return False

# TC = O(n+m)
# SC = O(26)

