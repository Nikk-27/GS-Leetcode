class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        for i in range(n):
            if tokens[i].lstrip('-').isdigit():
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == "+":
                    stack.append(a + b)
                elif tokens[i] == "-":
                    stack.append(a - b)
                elif tokens[i] == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack[-1]

# TC = O(N)
# SC = O(N)