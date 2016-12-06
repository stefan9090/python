class mystack(list):
    index = 0
    def __init__(self):
        self = []
        
    def __repr__(self):
        return str(self[:])
    
    def push(self, val):
        self.append(val)
        
    def peek(self):
        assert len(self) >0
        return self[-1]

    def is_empty(self):
        return len(self)==0

m = mystack()
mystack.push(m, 4)
print(m)
m.push(3)
m.push(5)
print(m.peek())
print(m.is_empty())
print(m.pop())
print(m.is_empty())
print(m.pop())
print(m.is_empty())
    
    
    # 
    
# def is_valid(haakjes):
    # buf_stack = mystack()
    # for a in haakjes:
        # if a=='(' or a=='{' or a=='[' or a=='<':
            # buf_stack.push(a)
        # elif a==')':
            # if mystack.peek()== '(':
                # buf_stack.pop()
        # elif a=='}':
            # if mystack.peek()== '{':
                # buf_stack.pop()
        # elif a==']':
            # if mystack.peek()== '[':
                # buf_stack.pop()
        # elif a=='>':
            # if mystack.peek()== '<':
                # buf_stack.pop()
    # if(buf_stack.is_empty()):
        # print(buf_stack)
        # return 0
    # else:
        # print(buf_stack)
        # return 1
# haakjes = '((())'

# hi = is_valid(haakjes)
# print(hi)        
