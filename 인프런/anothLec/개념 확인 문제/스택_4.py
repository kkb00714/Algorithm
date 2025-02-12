# 문제 3) 괄호 짝 맞추기
# 입력된 문자열이 ()로 이루어진 괄호인지 확인하고,
# 짝이 맞지 않거나 ((), 괄호가 이루어지지 않으면 )( 안됨.
# 올바른 괄호 문자열이라면 YES, 아니라면 NO 출력

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(items)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items.pop()


def is_valid_str(s):
    stack = Stack()

    for char in s:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty():
                retun "NO"
            stack.pop()

    # 스택이 비어있다면 올바른 괄호 문자열, 아니라면 NO
    return "YES" if stack.is_empty() else "NO"