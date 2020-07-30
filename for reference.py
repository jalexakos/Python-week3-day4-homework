# Linked List:

# A Complete Implementation of a LinkedList

# 2 Components to this solution -- A Node Class and the LinkedList class

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
    
    def pushOn(self,new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self,prev_node,new_value):
        # Check if the previous node even exists
        if prev_node is None:
            print("The given previous node must not be empty!")
            return
        # IF the Node is not empty, then create a new node
        new_node = Node(new_value)
        
        # Update the previous node's next pointer to point to the new value
        new_node.next = prev_node.next
        
        # Update the previous node to point to the new node's value
        prev_node.next = new_node
        
    # This method will append a new node to the END of the LinkedList
    def append(self,new_value):
        # Create New Node with a new value
        new_node = Node(new_value)
        
        # Check if the LinkedList is empty
        # And if it is, make THIS new node the head node(beginning of the list)
        if self.head is None:
            self.head = new_node
            
        # BUT if the list is NOT empty - traverse to the end
        # and add the NEW value to the end of the list
        
        last = self.head
        
        # While last.next is not None > continue to loop until we find a None value
        while(last.next):
            last = last.next
        # Change current last node value to point to the NEW value
        last.next = new_node
    
    def traverse(self):
        temp = self.head
        # while temp is NOT None -> keep looping through the links until you reach a None Value
        while(temp):
            print(temp.value)
            temp = temp.next

weekdays_links = LinkedList()

# Insert a new day into the list
weekdays_links.pushOn("Mon")
weekdays_links.append("Tues")
weekdays_links.append("Thurs")
weekdays_links.insertAfter(weekdays_links.head.next,"Wed")
weekdays_links.traverse()


# Binary Search Tree

class BST():
    def __init__(self,value):
        self.value = value # Current Value
        self.left = None
        self.right = None
        
    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self
    
    def contains(self,value):
        """
            This method accepts an int for its value
            The value parameter is what we are looking for inside of the BST structure
        """
        if value < self.value: # if passed value is less than current value
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True
        
        
    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()
        
    def getMaxValue(self):
        if self.right is None:
            return self.value
        else:
            return self.right.getMaxValue()
        
    def remove(self,value,parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value,self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value,self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value,self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    self.value = None
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self
    
bst_example = BST(39)
bst_example.insert(40)
bst_example.insert(50)
bst_example.insert(50)
bst_example.insert(50)
bst_example.insert(60)

print(bst_example.getMaxValue())
print(bst_example.contains(50))
print(bst_example.contains(44))
bst_example.remove(40)
print(bst_example.contains(40))
bst_example.remove(50)
print(bst_example.contains(50))