from queue import Queue


class Stack:
    def __init__(self):
        self.curr_size = 0
        self.q1 = []
        self.q2 = []


    def push(self,x):
        self.curr_size+=1

        self.q1.append(x)

    def pop(self):
        if self.q1 is None:
            return 

        while(len(self.q1)!=1):
            self.q2.append(self.q1[0]) #adding top elements into q2
            self.q1.pop(0)   #removing them from q1


        self.q1.pop(0)   #popping the only left elememt
        self.curr_size-=1 

        #rename the queues
        self.q  = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def getTop(self):
        if self.q1 is None:
            return
        
        return self.q1[-1]

    def display(self):
        if self.q1 is None:
            return 
        
        for i in range(len(self.q1)-1,-1,-1):
            print(self.q1[i],end=" ")


if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    s.display()
    print()
    print("Current_size",s.curr_size)

    s.pop()
    
    print("Current_size",s.curr_size)

    print("Top element is :",s.getTop())

    s.display()






