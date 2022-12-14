# Stack 

 * In computer science, a stack is an abstract data type that serves as a collection of elements, with two principal operations: push, which adds an element to the collection, and pop, which removes 
the most recently added element that was not yet removed.

 * see <a href="https://en.wikipedia.org/wiki/Stack_(abstract_data_type)">Stack (Wikipedia)</a>

### Stack Basic Operations

### Push 

> The operation to insert elements in a stack is called push. When we push the book on a stack, we put the book on the previous top element which means that the new book becomes the top element. This is what we mean when we use the push operation, we push elements onto a stack. We insert elements onto a stack and the last element to be pushed is the new top of the stack.

### Pop 
> Popping is when we take the top book of the stack and put it down. This implies that when we remove an element from the stack, the stack follows the **LIFO Last-In, First Out** property. This means that the top element, the last to be inserted, is removed when we perform the pop operation.

*Push and Pop are two fundamental routines that we’ll need for this data structure.*

### Peek 
> Another thing that we can do is view the top element of the stack, so we can ask the data structure: “What’s the top element?” and it can give that to us using the peek operation. Note that the peek operation does not remove the top element, it merely returns it.

##Time Complexities:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- isEmpty: O(1)
- Size: O(1)

###Limitations:
  - Stack size is to be defined first and cannot be changed.
  - Trying to push a new element into a full stack causes an implementation-specific exception.

##Applications of Stack:
- Balancing of symbols
- Infix-to-postfix conversion
- Evaluation of postfix expression
- Implementing function calls (including recursion)
- Page-visited history in a Web browser [Back Buttons]
- Undo sequence in a text editor
- Matching Tags in HTML and XML
- Used in many algorithms like Tower of Hanoi, tree traversals, stock span problem, histogram problem.