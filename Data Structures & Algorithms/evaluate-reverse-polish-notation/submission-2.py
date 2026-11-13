class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']

        for token in tokens:

            if token not in operands:
                stack.append(token) 
            # stack = [1, 2]

            else:
                elem1 = int(stack.pop())
                elem2 = int(stack.pop())
                
                if token == '+':
                    stack.append(elem2 + elem1)
                elif token == '-':
                    stack.append(elem2 - elem1)
                elif token == '*':
                    stack.append(elem2 * elem1)
                elif token == '/':
                    stack.append(elem2 / elem1)

        return int(stack.pop())


        