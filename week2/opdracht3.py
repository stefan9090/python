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
    
def is_valid(haakjes):
    stack = mystack()
    for a in haakjes:
        if a=='(' or a=='{' or a=='[' or a=='<':
            stack.push(a)
        elif stack.is_empty():
            return False
        elif a==')':
            if stack.peek()== '(':
                stack.pop()
        elif a=='}':
            if stack.peek()== '{':
                stack.pop()
        elif a==']':
            if stack.peek()== '[':
                stack.pop()
        elif a=='>':
            if stack.peek()== '<':
                stack.pop()     
    if(stack.is_empty()):
        print(stack)
        return True
    else:
        print(stack)
        return False
haakjes = '()))'

print(is_valid(haakjes))   
