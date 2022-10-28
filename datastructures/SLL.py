from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    
    def traverse_list(self):
        if self.head is None:
            print("List is empty!")
            return 
        else:
            temp = self.head.next
            #temp = self.head
            while temp:
                print(temp.data,end="->")
                temp = temp.next
                
                if temp == self.head.next:
                    break
                
            print("None")

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return 
        else:
            '''
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            '''
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def middle_element(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while fast_ptr.next is not None:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            print("The Middle Element is:",slow_ptr.data)
        else:
            print("list is empty")

    def insert_at_given_pos(self,x,data):
        if self.head is None:
            print("List is Empty")
            return
        new_node = Node(data)
        prev = None
        curr = self.head
        i = 0
        while i!=x:
            prev = curr
            curr = curr.next
            i+=1
        
        prev.next = new_node
        new_node.next = curr
        

    def reverse_list(self):
        if self.head is None:
            print("List is Empty")
            return
        
        next_node = None
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev        

    def search(self,x):
        if self.head is None:
            print("List is Empty!")
        
        temp = self.head
        i = 0 
        while temp is not None:
            if temp.data == x:
                print("%d element found at %d position" %(x,i) )
                break
            temp = temp.next
            i+=1
        else:
            print("Element %d not found" %(x))

    def delete_element(self,x):
        if self.head is None:
            print("List is Empty")
        prev = None
        curr = self.head 

        while curr.data != x:
            prev = curr
            curr = curr.next

        prev.next = curr.next
        del curr

    def count(self):
        if self.head is None:
            print("list is empty")
        
        i = 0 
        temp = self.head

        while temp is not None:
            temp = temp.next
            i+=1

        #print("Number of elements in the list %d" %(i))
        return i
    
    def detect_loop(self):
        sp = self.head
        fp = self.head

        while(sp and fp and fp.next):
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                self.remove_loop(sp)
                return 1
        else:
            return 0

    def remove_loop(self,loop_node):
        ptr1 = self.head

        while(1):
            ptr2 = loop_node

            while(ptr2.next!=loop_node and ptr2.next!=ptr1):
                ptr2 = ptr2.next

            if ptr2.next == ptr1:
                break

            ptr1 = ptr1.next

        ptr2.next = None

    '''
    def bubblesort(self):
        temp = self.head
        swap = None
        swapped = 1

        while(swapped):
            swapped = 0

            while(temp.next!=None):
                if(temp.data > temp.next.data):
                    swap = temp.data
                    temp.data = temp.next.data
                    temp.next.data = swap
                    swapped = 1
                temp = temp.next
            temp = self.head


    def removeduplicates(self):
        if self.head == None:
            print("list is empty")

        else:
            temp = self.head
            while(temp.next!=None):
                start = temp
                while(start.data==start.next.data):
                    start = start.next

                temp.next = start.next
                temp = start.next
    '''
    def remDuplicates(self):
        if self.head is None:
            print("list is empty")
        
        myset = set()
        cur = self.head
        myset.add(cur.data)

        while cur.next:
            if cur.next.data in myset:
                cur.next = cur.next.next
            else:
                myset.add(cur.next.data)
                cur = cur.next
    
    def kToLastElement(self,k):
        if self.head is None:
            print("list is empty")
        len = self.count()
        print(len)
        cur = self.head
        while k-1>0:
            if k<len:
                cur = cur.next
                k-=1
            else:
                print("{} is greater than length {} of the list".format(k,len))
                break
        while cur:
            print(cur.data,end="->")
            cur = cur.next
        
    def deleteNode(self,node):
        if self.head is None:
            print("list is empty")
        cur = self.head

        while cur.next.data!=node.data:
            cur = cur.next
        cur.next = node.next

    def isPalindrome(self):
        if self.head is None:
            print("Is Palindrome")
        cur = self.head
        stack = deque()

        while cur:
            stack.append(cur.data)
            cur = cur.next
        cur = self.head

        while cur.next and stack:
            if cur.data == stack.pop():
                cur = cur.next
            else:
                print("Is not a palindrome")
                break
        else:
            print("Is a palindrome")
    

if __name__ == "__main__":

    sll = SingleLinkedList()
    sll.insert_at_end('A')
    sll.insert_at_end('B')
    sll.insert_at_end('C')
    sll.insert_at_end('D')
    sll.insert_at_end('E')
    sll.insert_at_end('C')
    

    
    sll.traverse_list()

    #sll.isPalindrome()
    #sll.deleteNode(sll.head.next.next.next.next)
    #sll.remDuplicates()
    #sll.bubblesort()

    #k = int(input("Enter the k"))
    #sll.kToLastElement(k)

    #sll.removeduplicates()
    #creating a loop
    #sll.head.next.next.next.next = sll.head.next

    #sll.detect_loop()
    #sll.removeduplicates()

    #sll.traverse_list()
    
    '''
    sll = SingleLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_end(4)
    sll.insert_at_end(5)

    SingleLinkedList.traverse_list(sll)

    sll.traverse_list()    
    SingleLinkedList.reverse_list(sll)
    sll.middle_element()
    SingleLinkedList.traverse_list(sll)
    SingleLinkedList.search(sll,3)
    SingleLinkedList.insert_at_given_pos(sll,4,7)
    SingleLinkedList.traverse_list(sll)
    SingleLinkedList.delete_element(sll,7)
    SingleLinkedList.traverse_list(sll)
    SingleLinkedList.count(sll)

    
    sll.reverse_list()
    sll.traverse_list()
'''
