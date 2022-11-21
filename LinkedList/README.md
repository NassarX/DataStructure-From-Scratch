# LinkedList 

### Structure
> Every linked list consists of nodes, as shown in the illustration above. Every node has two components:

- Data
- Next
> The **data** component allows a node in the linked list to store an element of data that can be of type string, character, number, or any other type of object.

> The **next** component in every node is a **pointer** that points from one node to another.

> The **start** of the linked list is referred to as the head. **head** is a pointer that points to the beginning of the linked list, so if we want to traverse the linked list to obtain or access an element of the linked list, we’ll start from head and move along.

> The **last** component of a singly linked list is a notion of **null**. This null idea terminates the linked list. In Python, we call this None. The last node in a singly linked list points to a null object, and that tells you that it’s the end of the linked list.

### LinkedList Types :

###1. Singly Linked Lists
###2. Doubly Linked Lists
###3. Circular Linked List

### LinkedList Operations :

1. Append
   - The append method will insert an element at the end of the linked list.
   
2. Prepend
   - The prepend method will insert an element at the beginning of the linked list.

3. Insert After Node Prepend 
   - Inserting an element after a given node.

4. Insert Before Node
   - Inserting an element before a given node.

5. Deletion by Value
   - Delete the node by its value and update the rest of the pointers.

6. Deletion by Position
   - Delete the node by its index and update the rest of the pointers.