class Solution:
    def isValid(self, s: str) -> bool:
        
        arr = [0]*len(s)
        cap = len(s)
        top = -1

        for i in s:
            if i == '(' or i == '{' or i =='[':
                top += 1
                arr[top] = i

            elif i == ')' or i == '}' or i ==']':
                if top == -1:
                    return False
                recent = arr[top]
                
                arr[top] = None
                top -=1

                if i == ')' and recent == '(':
                    continue

                elif i == '}' and recent == '{':
                    continue

                elif i == ']' and recent == '[':
                    continue
                
                else:
                    return False
                
        return top == -1