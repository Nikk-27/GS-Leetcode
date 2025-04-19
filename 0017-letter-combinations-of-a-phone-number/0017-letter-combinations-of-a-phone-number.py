class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitstochar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return

            for c in digitstochar[digits[i]]:
                backtrack(i+1, cur+c)
        if digits:
            backtrack(0, '')
        return res

# TC = 4^n * n
# 4 character options to choose for each digit (see 7,9) therefore 4^n options, then O(n) it takes to append to res

# SC = 4^n * n
# 4^n options each of length n