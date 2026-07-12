class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token !='+' and token!='-' and token !='*' and token !='/':
                stack.append(int(token))
            else :
                if token=='+':
                    stack.append(stack.pop() + stack.pop())
                elif token=='-':
                    num2=stack.pop()
                    num1=stack.pop()
                    stack.append(num1 - num2)
                elif token=='*':
                    stack.append(stack.pop() * stack.pop())
                elif token=='/':
                    num2=stack.pop()
                    num1=stack.pop()
                    stack.append(int(num1 / num2))
        return int(stack.pop())
                


        