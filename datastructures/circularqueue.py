#circular queue using list in python

class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.myqueue = [None for i in range(size)]
        self.rear = -1
        self.front = -1


    def enqueue(self,data):

        #check it is full or not
        if (self.rear+1)%self.size == self.front:
            print("Queue is full")

        #first time you are inserting
        if(self.rear == -1):
            self.rear = 0
            self.front = 0
            self.myqueue[self.rear] = data
        
        else:
            self.rear = (self.rear+1) % self.size
            self.myqueue[self.rear] = data

        
    def dequeue(self):
        if (self.front == -1):
            print("Queue is Empty")

        #if only one element
        elif (self.front == self.rear):
            temp = self.myqueue[self.front]
            self.rear = -1
            self.front = -1
            return temp

        else:
            temp = self.myqueue[self.front]
            self.front = (self.front + 1) % self.size
            return temp


    def display(self):
        if(self.front == -1):
            print("Queue is Empty")

        elif (self.rear>=self.front):
            print("Elements in the queue are:")
            for i in range(self.front,self.rear+1):
                print(self.myqueue[i],end=" ")

            print()

        else:
            print("Elements in the queue are:")
            for i in range(self.front,self.size):
                print(self.myqueue[i],end=" ")

            for i in range(0,self.rear+1):
                print(self.myqueue[i],end=" ")

            print()



if __name__ == "__main__":
    myqueue = CircularQueue(5)
    myqueue.enqueue(14)
    myqueue.enqueue(22)
    myqueue.enqueue(13)
    myqueue.enqueue(-6)
    myqueue.enqueue(90)
    myqueue.display()

    print("deleted value is :",myqueue.dequeue())

    myqueue.display()

