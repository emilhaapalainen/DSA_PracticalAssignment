class Node:
    def __init__(self, data, next):     #Initializing the node.
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):    #Initializing the linked list.
        self.head = None
    
    #Search function for searching data from the list. Returns True if found, False if not found.
    def search(self, data):    
        curr = self.head       
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def print(self):    #Print function for the list. Prints a list of all the data that is in each list. 
        headnode = self.head
        while headnode:
            print(headnode.data, end=' ')
            if headnode.next != None:
                print('->', end=' ')
            headnode = headnode.next
    
    def insertEnd(self, data):     #Inserting data to the end of the list. 
        temp = self.head
        while temp != None:
            if temp.data == data:
                return
            temp = temp.next
        newNode = Node(data, None)
        if self.head != None:
            tempNode = self.head
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next = newNode
        else:
            self.head = newNode
    
    #Deleting data from the list. The temporary variable allows the previous node to point to the next node.
    def delete(self, data):     
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        tempNode = self.head
        while tempNode.next != None:
            if tempNode.next.data == data:
                tempNode.next = tempNode.next.next
                return
            tempNode = tempNode.next
    

class HashTable:
    def __init__(self, size):  #Initializing the hash table. The size of the table is given as a parameter.
        self.size = size
        self.Table = [LinkedList() for i in range(0,self.size)]
    '''
    The hash function converts the fed data into an integer value and raises it to the power of 4.
    After that the total is divided by the size of the hash table and the remainder is returned and used as the index value for the stored data.
    '''
    def hash(self, data):   
        data = str(data)
        total = 0
        for i in range(len(data)):
            value = int(ord(data[i]))
            total += value**4
        final = total % self.size
        return final

    def print(self):    #Printing function for the hash table. Prints the index and the data in each list.
        for i in range(0,self.size):
            if self.Table[i].head != None:
                print('Location index:', i, end=' ')
                self.Table[i].print()
                print()
        
    def insert(self, data):     #Data insert function for the hash table.
        index = self.hash(data)
        self.Table[index].insertEnd(data)

    def search(self, data):     #Search function for the hash table. Returns True if found, False if not.
        index = self.hash(data)
        return self.Table[index].search(data)
    
    def delete(self, data):     #Delete function for the hash table.
        index = self.hash(data)
        self.Table[index].delete(data)

#Usage:
 #table = HashTable(8) Initializes the hash table with a size of 8.
 #table.insert(data) Inserts data into the hash table.
 #table.search(data) Searches for data in the hash table. Returns True if found, False if not.
 #table.delete(data) Deletes data from the hash table.
 #table.print() Prints out the hash table.
