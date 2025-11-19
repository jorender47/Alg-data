class Node:
 def __init__(self, element):
 self.elmenet = element
 self.next = None

 #Step 1: Declare head and tail:
 head = None
 tail = None

 #Step 2: Create the first node and add it to the list
 head = Node("Chicago")
 last = head

 #Step 3 : Create the second node and add it to the list
 tail.next = Node("Denver")
 tail = tail.next

 # Step 4 : Create the third node and add it to the list
 tail.next = Node("Dalles")
 tail = tail.next

#TRAVERSING ALL ELEMENTS IN THE LIST
current = head
while current != None:
    print(current.element)
    current = current.next

#IMPLEMENTING ADDFIRST(E
def addFirst(self,e):
    newNode = Node(e) # Create a new node
    newNode.next = self.__head # link the new node with the head
    self.__head = newNode # head points to the new node
    self.__size += 1 # Increase list size
    if self.__tail == None: # the new node is the only node in list
        self.__tail = self.__head

#IMPLEMENTING ADDLAST(E)
def addLast(self, e):
 newNode = Node(e) # Create a new node for e
 if self.__tail == None:
    self.__head = self.__tail = newNode # The only node in list
 else:
    self.__tail.next = newNode # Link the new with the last node
    self.__tail = self.__tail.next # tail now points to the last node
 self.__size += 1 # Increase size

#IMPLEMENTING ADD(INDEX, E)
def insert(self, index, e):
 if index == 0:
    self.addFirst(e) # Insert first
 elif index >= size:
    self.addLast(e) # Insert last
 else: # Insert in the middle
    current = head
    for i in range(1, index):
        current = current.next
    temp = current.next
    current.next = Node(e)
    (current.next).next = temp
    self.__size += 1

#IMPLEMENTING REMOVEFIRST()
def removeFirst(self):
 if self.__size == 0:
    return None
 else:
    temp = self.__head
    self.__head =
    self.__head.next self.__size -= 1
 if self.__head == None:
    self.__tail = None return temp.element

#IMPLEMENTING REMOVELAST()
def removeLast(self):
 if self.__size == 0:
    return None
 elif self.__size == 1:
    temp = self.__head
    self.__head = self.__tail = None
    self.__size = 0
    return temp.element
 else:
    current = self.__head
    for i in range(self.__size - 2):
        current = current.next
    temp = self.__tail
    self.__tail = current
    self.__tail.next = None
    self.__size -= 1
    return temp.element

 #IMPLEMENTING REMOVEAT(INDEX)
def removeAt(self, index):
 if index < 0 or index >= self.__size:
    return None # Out of range
 elif index == 0:
    return self.removeFirst() # Remove first
 elif index == self.__size - 1:
    return self.removeLast() # Remove last
 else:
    previous = self.__head
    for i in range(1, index):
        previous = previous.next
    current = previous.next
    previous.next = current.next
    self.__size -= 1
    return current.element

