from collections import deque

class Stack:
    def __init__(self,size=None):
        if size==None:
            self.mystack = deque()
            self.size = 0
        else:
            self.size = size
            self.mystack = deque(maxlen=size)

    def push(self,element):
        if len(self.mystack) == self.size:
            print("Cannot add more element, stack full")
        else:

            self.mystack.append(element)

    def pop(self):
        if len(self.mystack) == 0:
            print("Stack is empty,cannot pop")
        else:
            return self.mystack.pop()

    def peek(self):
        if len(self.mystack) == 0:
            print("Stack is empty")
        else:
            return self.mystack[-1]
    
    def display(self):
        if len(self.mystack) == 0:
            print("Stack is empty bruh")
        else:
            print("Your stack is:")
            for i in range(len(self.mystack)-1,-1,-1):
                print(self.mystack[i],end=" ")
    
    def sortStack(self):
        t = Stack()
        
        while len(self.mystack)!=0:
            temp_number = self.pop()
            #print(temp_number,end=" ")

            while len(t.mystack)!=0 and int(t.peek()) > int(temp_number):
                element = t.pop()
                self.push(element)

            t.size+=1  
            #print(temp_number,end=" ")
            t.push(temp_number)
            
        return t

if __name__ == "__main__":
    '''    
    size = int(input("Enter the size of the stack you want"))
    s = Stack(size)
    for _ in range(size):
        print("Enter element to push")
        s.push(int(input()))

    #print("Popped element is:",s.pop())
    #print("Top element is:",s.peek())
    '''
    s = Stack(4)
    s.push(4)
    s.push(7)
    s.push(3)
    s.push(10)
    #s.push(92)
    #s.push(23)

    s.display()
    print()
    temp = s.sortStack()
    print()
    print("Sorted stack")
    temp.display()




