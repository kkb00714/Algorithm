# 문제 2) 마지막 남은 카드

# 1부터 N까지의 숫자가 적힌 카드 더미가 있다.
# 각 턴마다 가장 위의 카드를 버리고,
# 다음 카드를 카드 더미의  맨 아래로 이동한다.
# 이 과정을 반복했을 때 마지막으로 남는 숫자를 출력하자.

# input : 7
# output : 6

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
        return self.items.pop(0)


def last_card(n):
    stack = Stack()
    
    for i in range(1, n+1):
        stack.push(i)

    while len(stack.items) > 1:
        stack.pop()
        stack.push(stack.pop())

    return stack.pop()

print(last_card(7))