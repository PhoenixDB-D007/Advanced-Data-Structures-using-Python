def insert_data(_data):
        mytree = AVL_Tree()
        root = None
        for i in _data:
            root = mytree.insert(root,i)
        print("Preorder Traversal of constructed AVL tree is:")
        mytree.preOrder(root)
        print()
        return root
def Search(root,val):
    if (root is None):
        return False
    elif (root.val == val):
        return True
    elif(root.val < val):
        return Search(root.right,val)
    return Search(root.left,val)
    return False

def main():
    root = insert_data([105,86,175,77,89,9120])
    t = int(input('Enter the key to be searched:\t'))
    if(Search(root,t)):
        print()
        print('"Element found in AVL Tree"')
    else:
        print()
        print('"Element not found in AVL Tree"')
if __name__ == "__main__":
    main()
else:
    pass
