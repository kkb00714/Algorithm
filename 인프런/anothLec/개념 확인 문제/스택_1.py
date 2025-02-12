# Stack(스택) - 후입선출(Last In First Out, LIFO)

# 1) 기본적인 스택 클래스 구조
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

    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return self.items[-1]

    

# 2) 스택 사용 방식
stack = Stack()


# 2-1) push(item) :  스택의 가장 윗부분에 항목 삽입
stack.push(10)
stack.push("hi")
stack.push(20)
stack.push("Stack")
print(stack.items)  # [10, 'hi', 20, 'Stack']


# 2-2) pop(item) :  스택에서 가장 위에 있는 항목 제거
popped_item = stack.pop()
print(popped_item)  # Stack
print(stack.items)  # [10, 'hi', 20]


# 2-3) peek() :  스택의 가장 위에 있는 항목 반환 (값 제거 x)
top_item = stack.peek()
print(top_item) # 20
print(stack.items) # [10, 'hi', 20]


# 2-4) is_empty() :  스택이 비어있을 때 true 반환
print(stack.is_empty()) # False

stack.pop()
stack.pop()
stack.pop()

print(stack.is_empty()) # True
