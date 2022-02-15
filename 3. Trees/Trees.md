# Topic - TREES

|Content Table|
| :----------|
|[1. Intro](#binary-tree)|
|[2. Properties](#properties-of-binary-trees)|
|[3. Types](#types-of-binary-trees)|

## BINARY TREE

A tree whose elements have at most 2 children is called a binary tree. 
A Binary Tree node contains following parts.

a. Data

b. Pointer to left child

c. Pointer to right child

```
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
```

Unlike Arrays, Linked Lists, Stack and queues, which are linear data structures, trees are _hierarchical data structures_.


### Why Trees? 

1. One reason to use trees might be because you want to store information that naturally forms a hierarchy.
2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays). 
3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists). 
4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on number of nodes as nodes are linked using pointers.


### Properties of Binary Trees

1. The maximum number of nodes at level ‘l’ of a binary tree is **2l**. 
2. The Maximum number of nodes in a binary tree of height ‘h’ is **2h – 1**. 
3. In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is **Log2(N+1)**   
4. A Binary Tree with l leaves has at least **|Log2L|+1**   levels 
5. In Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more than nodes with two children.

/
### _TYPES OF BINARY TREES_

### 1. Full Binary Tree 

A Binary Tree is a full binary tree if every node has 0 or 2 children. The following are the examples of a full binary tree. We can also say a full binary tree is a binary tree in which all nodes except leaf nodes have two children. 
```
               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40

             18
           /    \   
         15     20    
        /  \       
      40    50   
    /   \
   30   50

               18
            /     \  
          40       30  
                   /  \
                 100   40
```
### 2. Complete Binary Tree 

A Binary Tree is a Complete Binary Tree if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible.
```
              18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40


               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40
     /  \   /
    8   7  9 
```
### 3. Perfect Binary Tree 

A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level. 
```
               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40


               18
           /       \  
         15         30  
```
- In a Perfect Binary Tree, the number of leaf nodes is the number of internal nodes plus 1  

### 4. Balanced Binary Tree 

A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes. 

For Example, the AVL tree maintains O(Log n) height by making sure that the difference between the heights of the left and right subtrees is at most 1. Red-Black trees maintain O(Log n) height by making sure that the number of Black nodes on every root to leaf paths is the same and there are no adjacent red nodes. Balanced Binary Search trees are performance-wise good as they provide O(log n) time for search, insert and delete. 

### 5. A Degenerate (or Pathological) Tree 

A Tree where every internal node has one child. Such trees are performance-wise same as linked list. 
```
      10
      /
    20
     \
     30
      \
      40     
```

## TREE TRAVERSALS
Example Image:

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif" />


### Depth First Traversals: 

(a) Inorder (Left, Root, Right) : 4 2 5 1 3 

(b) Preorder (Root, Left, Right) : 1 2 4 5 3 

(c) Postorder (Left, Right, Root) : 4 5 2 3 1

* INORDER TRAVERSAL -
```
Algorithm Inorder(tree)
   1. Inorder(left-subtree)
   2. Visit the root.
   3. Inorder(right-subtree)
```

* PREORDER TRAVERSAL -
```
Algorithm Preorder(tree)
   1. Visit the root.
   2. Preorder(left-subtree)
   3. Preorder(right-subtree) 
```

* POSTORDER TRAVERSAL -
```
Algorithm Postorder(tree)
   1. Postorder(left-subtree)
   2. Postorder(right-subtree)
   3. Visit the root.
```

### Inorder Traversal Without Recursion using a stack 


```
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current -> left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item -> right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
```
Python Code
```
def inOrder(root):
     
    current = root
    stack = []
     
    while True:

        if current is not None:
            stack.append(current)
            current = current.left

        elif(stack):
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
 
        else:
            break
      
    print()
 ```
### Inorder Traversal Without Recursion and Without stack 

The idea of **Morris Traversal** is based on **Threaded Binary Trees**. A threaded binary tree is a binary tree variant that facilitates traversal in a particular order.
<IMG SRC="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Threaded_tree.svg/330px-Threaded_tree.svg.png" />

 ```
1. Initialize current as root 
2. While current is not NULL
   If the current does not have left child
      a) Print current’s data
      b) Go to the right, i.e., current = current->right
   Else
      a) Find rightmost node in current left subtree OR
              node whose right child == current.
         If we found right child == current
             a) Update the right child as NULL of that node whose right child is current
             b) Print current’s data
             c) Go to the right, i.e. current = current->right
         Else
             a) Make current as the right child of that rightmost 
                node we found; and 
             b) Go to this left child, i.e., current = current->left
```
```
def morris_traversal(root):
    current = root
  
    while current is not None:
  
        if current.left is None:
            yield current.data
            current = current.right
        else:
            pre = current.left
            while pre.right is not None 
                  and pre.right is not current:
                pre = pre.right
  
            if pre.right is None:
                pre.right = current
                current = current.left
  
            else:
                pre.right = None
                yield current.data
                current = current.right
```