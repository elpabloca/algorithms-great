# algorithms-great


This is a repo to practice and enjoy some basic algorithms that are used in developer's life

We have in some languages, mainly in Javascript(NodeJS), Python and maybe Golang!

### What is big O notation ?

<h4>Big O notation is special notation that tells you how fast an algorithm is.</h4>

Here are five big O run times that you’ll encounter a lot, sorted from
fastest to slowest:

- O(log n): also known as log time. Example: binary search.
- O(n): also known as linear time. Example: simple search.
- O(n * log n): Example: a fast sorting algorithm, like quicksort.
- O(n^2): Example: a slow sorting algorithm, like selection sort.
- O(n!): n factorial, Example: a really slow algorithm, like the traveling salesperson.

Notes:

- Binary search is a lot faster than simple search as your array gets
bigger.
O(log n) is faster than O(n), and it gets a lot faster once the list of
items you’re searching through grows.
- Algorithm speed isn’t measured in seconds.
- Algorithm times are measured in terms of growth of an algorithm.
- Algorithm times are written in big O notation.

## Selection sort

- Your computer’s memory is like a giant set of drawers.
- When you want to store multiple elements, use an array or a linked
list.
- With an array, all your elements are stored right next to each other.
- With a linked list, elements are strewn all over, and one element stores
the address of the next one.
- Arrays allow fast reads.
- Linked lists allow fast inserts and deletes.

## Recursion

- Recursion is when a function calls itself.
- Every recursive function has two cases: the base case and the recursive case.
- A stack has two operations: push and pop.
- All function calls go onto the call stack.
- The call stack can get very large, which takes up a lot of memory.