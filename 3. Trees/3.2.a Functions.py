class node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

# Insert a value into BST
    def insert(self,data):
        if self.root==None:
            self.root=node(data)
        else:
            curent=self
            while 1:
                if data < current.data:
                    if current.left:
                        current=current.left
                    else:
                        new=node(data)
                        current.left=new
                        break
                elif data > current.data:
                    if current.right:
                        current=current.right
                    else:
                        new=node(data)
                        current.right=new
                        break
                else:
                    break

# Search for a value in BST (Binary Search)
    def search(self,target):
        if self.data==target:
            return self
        if self.left and self.data>target:
            return self.left.search(target)
        if self.right and self.data<target:
            return self.right.search(target)
    
# PREORDER TRAVERSAL
    def preorder(self):
        print(self.data)
        if self.left:
            self.preorder(self.left)
        if self.right:
            self.preorder(self.right)

# POSTORDER TRAVERSAL    
    def postorder(self):
        if self.left:
            self.postorder(self.left)
        if self.right:
            self.postorder(self.right)
        print(self.data)

# INORDER TRAVERSAL
    def inorder(self):
        if self.left:
            self.inorder(self.left)
        print(self.data)
        if self.right:
            self.inorder(self.right)

# FIND HEIGHT OF THE TREE
    def height(self,h=0):
        lheight=self.left.height(h+1) if self.left else h
        rheight=self.right.height(h+1) if self.right else h
        return max(lheight,rheight)

# GET NODES AT GIVEN DEPTH
    def getnodesatdepth(self,depth,nodes=[]):
        if depth==0:
            nodes.append(self.val)
            return nodes
        if self.left:
            self.left.getnodesatdepth(depth-1,nodes)
        if self.right:
            self.right.getnodesatdepth(depth-1,nodes)
        return nodes
