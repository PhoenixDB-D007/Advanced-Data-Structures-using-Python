class BST_Insert:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
  
def insert(root, key):
    if root is None:
        return BST_Insert(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
  
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
r = BST_Insert(5)
r = insert(r, 3)
r = insert(r, 50)
r = insert(r, 44)
r = insert(r, 72)
r = insert(r, 654)
r = insert(r, 821)

inorder(r)
