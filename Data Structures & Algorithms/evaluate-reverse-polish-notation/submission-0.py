import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        stack=[]
        for elem in tokens:
            if elem in operators:
                func = operators[elem]
                operand_a=stack.pop()
                operand_b=stack.pop()
                result =int( func(operand_b,operand_a))
                stack.append(result)
            else:
                stack.append(int(elem))
        return stack[-1]
        