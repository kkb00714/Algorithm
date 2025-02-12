# 문제 1) 스택을 이용한 문자열 뒤집기

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items.pop()
    

def reverse_string(s):
    stack = Stack()

    for char in s:
        stack.push(char)

    reversed_s = ""
    while not stack.is_empty():
        reversed_s += stack.pop()

    return reversed_s

user_input = input()
print(reverse_string(user_input))
