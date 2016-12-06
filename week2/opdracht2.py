class mystack():
    stack = []
    index = 0
    def __init__(self):
        mystack.stack = []
        
    def __repr__(self):
        return str(mystack.stack)
    
    def push(self, val):
        mystack.stack.append(val)

    def pop(self):
        if(len(mystack.stack)==0):
            return 0
        to_return = mystack.stack[-1]
        del mystack.stack[-1]
        return to_return
    
    def peek():
        if(len(mystack.stack)==0):
            return 0
        to_return =  mystack.stack[-1]
        return to_return
    
    def is_empty(self):
        if(len(mystack.stack)):
            return 1
        return 0
    
def is_valid(haakjes):
    buf_stack = mystack()
    for a in haakjes:
        if a=='(' or a=='{' or a=='[' or a=='<':
            buf_stack.push(a)
        elif a==')':
            if mystack.peek()== '(':
                buf_stack.pop()
        elif a=='}':
            if mystack.peek()== '{':
                buf_stack.pop()
        elif a==']':
            if mystack.peek()== '[':
                buf_stack.pop()
        elif a=='>':
            if mystack.peek()== '<':
                buf_stack.pop()
    if(buf_stack.is_empty()):
        print(buf_stack)
        return 0
    else:
        print(buf_stack)
        return 1
haakjes = '((())'

hi = is_valid(haakjes)
print(hi)        
