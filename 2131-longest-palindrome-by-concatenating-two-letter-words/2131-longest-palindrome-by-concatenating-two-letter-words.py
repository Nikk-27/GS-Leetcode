class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        #going with very simple approach <<hashing>>

        hash = Counter(words)
        size = 0

        for word in list(hash.keys()):
            rev = word[::-1]
            if rev != word:
                pair = min(hash[rev], hash[word])
                # rev + word adds 4 letters to result
                size += pair * 4
                hash[word] -= pair
                hash[rev] -= pair
            else:
                # reflexive words like aa, bb
                pair = hash[word] // 2
                size += pair * 4
                hash[word] -= pair * 2 #becaz 2 words like aa are used in result

        for word in words:
            # if any single pair remained left out
            if word[0] == word[1] and hash[word] > 0: 
                size += len(word)
                break # we just can add one reflexive piece in middle not all

        return size

# TC: O(n) — We iterate over all words once and process them in constant time.
# SC: O(n) — For storing word frequencies.
