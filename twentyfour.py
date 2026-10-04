# Implement of Stack in Python 
class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        return self.s.pop()

    def peek(self):
        return self.s[-1]

    def is_empty(self):
        return len(self.s) == 0

st = Stack()
st.push(1)
st.push(2)
print(st.pop())      
print(st.peek())     
print(st.is_empty()) 