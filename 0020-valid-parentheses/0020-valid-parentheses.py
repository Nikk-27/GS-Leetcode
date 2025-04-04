class Solution:
    def isValid(self, s: str) -> bool:
        temp = { ')' : '(', '}' : '{', ']' : '['}
        stack = []

        for i in s:
            if stack and i in temp.keys() and stack[-1] == temp[i] :
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0

# TC = O(N)
# SC = O(N)
