#trying to create a linked list 
#using theory concept 

#class node --> each node contains both head and next in linked list  

class Node:
    #intializing the head value and next value by default to none
    def __init__(self, data = None, next = None):
        #two class members
        self.data = data
        self.next = next

#class linked list --> pointinng to head of linked list 
class Linkedlist:
    def __init__(self):
        self.head = None

    #creating method to insert values at begining  -->replacing head here(start)
    def push_at_beginning(self, new_data):
        new_node = Node(new_data, self.head)  
        self.head = new_node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    #method to insert values at ending 
    def push_at_end(self,new_data):
        #if head none -- mean list is empty
        if self.head is None:
            self.push_at_beginning(new_data)
            return
        
        #if list is not empty-->making it iterable till end and adding at next 
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(new_data,None)   #next of last element

    #inserting values and creating lst  --> making hhead to none to create list from start
    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.push_at_end(data)

    #method to fetch lngth -> using count and iterating using intial = head and itr over next 
    def getLength(self):
        count=0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    #creating a custome remove function with index as an argumnt
    def remove_at(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception('invalid index')
        if index == 0 :
            self.head = self.head.next
            return
        
        #traverse loop
        prev = self.head
        itr = self.head
        currentIndex = 0
        while itr:
            if currentIndex == index:
                prev.next = itr.next
                break
            prev = itr
            itr = itr.next
            currentIndex += 1
            

if __name__ == "__main__":
    l1 = Linkedlist()
    l1.push_at_beginning('25')
    l1.push_at_beginning('30')
    l1.push_at_end('456')
    l1.print()
    l1.insertValues(['dhanush', 'reddy', 'singamala', 'marks','100/100'])
    l1.print()
    l1.remove_at(3)
    l1.print()

