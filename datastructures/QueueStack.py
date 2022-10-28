
class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self,x):
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())


    def dequeue(self):
        if not self.s1:
            return "Queue is empty"
        else:
            return self.s1.pop()
    
    def display(self):
        if not self.s1:
            print("Queue is empty")

        for i in range(len(self.s1)-1,-1,-1):
            print(self.s1[i],end='->')

if __name__ == "__main__":

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    #print("Size of the queue",q.size)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    #print("Size of the queue",q.size)
    print(q.dequeue())
    q.enqueue(10)
    q.enqueue(100)

    
    q.display()


