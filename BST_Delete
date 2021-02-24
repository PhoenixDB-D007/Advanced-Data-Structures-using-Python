class Node: 
    def inti(self,data): 
        self.data = data 
        self.left = None
        self.right = None 
def inorder(temp): 
    if(not temp): 
        return
    inorder(temp.left) 
    print(temp.data, end = " ") 
    inorder(temp.right) 
def deletion(root,d_node): 
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp is d_node: 
            temp = None
            return
        if temp.right: 
            if temp.right is d_node: 
                temp.right = None
                return
            else: 
                q.append(temp.right) 
        if temp.left: 
            if temp.left is d_node: 
                temp.left = None
                return
            else: 
                q.append(temp.left) 
def delete(root, key): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.key == key :  
            return None
        else : 
            return root 
    key_node = None
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp.data == key: 
            key_node = temp 
        if temp.left: 
            q.append(temp.left) 
        if temp.right: 
            q.append(temp.right) 
    if key_node :  
        x = temp.data 
        deletion(root,temp) 
        key_node.data = x 
    return root
if __name__=='__main__': 
    root = Node(12) 
    root.left = Node(9) 
    root.left.left = Node(7) 
    root.left.right = Node(13) 
    root.right = Node(6) 
    root.right.left = Node(15) 
    root.right.right = Node(4) 
    print("The tree before the deletion:") 
    inorder(root) 
    key = 6
    root = delete(root, key) 
    print() 
    print("The tree after the deletion;") 
    inorder(root) 
