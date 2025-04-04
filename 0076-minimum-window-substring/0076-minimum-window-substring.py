class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1 = {}
        count2 = {}
        res = float('inf')
        ans = ""
        for c in t:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        cur = 0
        i = 0
        for j in range(len(s)):
            count2[s[j]] = 1 + count2.get(s[j], 0)
            if count1.get(s[j], 0) == count2[s[j]]:
                cur += 1
                while cur == need:
                    if res > j-i+1:
                        res = j-i+1
                        ans = s[i:j+1]
                    count2[s[i]] -= 1
                    if s[i] in count1 and count1[s[i]] > count2[s[i]]:
                        cur -= 1
                    i += 1

        return ans

