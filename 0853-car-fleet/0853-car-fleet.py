class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = list()
        a = sorted(zip(position, speed))
        for i,j in a[::-1]: # Reverse sorted order
            stack.append((target-i)/j)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)