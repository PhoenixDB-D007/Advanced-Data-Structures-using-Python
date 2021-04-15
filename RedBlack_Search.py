class Node(object):
    def __init__(self, val, parent, color):
        self.val = val
        self.left = None
        self.right = None
        self.color = color
        self.parent = parent

class RB_tree(object):
    #RR rotation:
    def RR(self,node):
            t = node.left
            parent = node.parent
            p = t.right
            t.right = node
            node.left = p
            return t
        
    #LL rotation:
    def LL(self,node):
            t = node.right
            p = t.left
            t.left = node
            node.right = p
            return t

    #LR rotation:    
    def LR(self,node):
        t = node.right
        null = node.left
        p = t.left
        p.right = t
        p.left = node
        node.right = null
        t.left = null
        return p

    #RL rotation
    def RL(self,node):
        t = node.left
        null = node.right
        p = t.right
        p.left = t
        p.right = node
        node.left = null
        t.right = null
        return p

    def Balance(self,root,node):
        if (node.parent is None):
            return root
        #If node's parent is black no need of balancing:
        if(node.parent.color == 'B'):
            return root
        
        #loop till node is not root and node's parent color is red:
        while (node.parent != None) and (node.parent.color == 'R'):
            #get the uncle node :
            if (node.parent == node.parent.parent.left):
                uncle = node.parent.parent.right
                 #case: when uncle is absent or black: 
                if(uncle == None) or (uncle.color == 'B'):
                    if(node.parent.parent.parent == None) and (node != node.parent.right):
                        if(root.right == node.parent):
                            tnode = self.RR(node.parent.parent)
                            color = tnode.color
                            tnode.parent = None
                            tnode.right.parent = tnode
                            tnode.color = tnode.right.color
                            tnode.right.color = color
                            root = tnode
                            return root
                            
                    elif(node != node.parent.right):
                        if(node.parent.parent.parent.right == node.parent.parent):
                            tnode = self.RR(node.parent.parent)
                            node.parent.parent.parent.right = tnode
                        else:
                            tnode = self.RR(node.parent.parent)
                            node.parent.parent.parent.left = tnode
                    if(node == node.parent.right):
                        if(node.parent.parent.parent.right == node.parent.parent):
                            tnode = self.RL(node.parent.parent)
                            node.parent.parent.parent.right = tnode
                        else:
                            tnode = self.RL(node.parent.parent)
                            node.parent.parent.parent.left = tnode
                            
                    tnode.parent = node.parent.parent.parent
                    tnode.right.parent = tnode
                    tnode.left.parent = tnode
                    color = tnode.color
                    tnode.color = tnode.right.color
                    tnode.right.color = color
                    return root
                elif(uncle != None) and (uncle.color == 'R'):
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    if(node.parent.parent.parent != None):
                        node.parent.parent.color = 'R'
                        node = node.parent.parent
                    else:
                        break
                        
                        
            else:
                if(node.parent == node.parent.parent.left):
                    uncle = node.parent.parent.right
                else:
                    uncle = node.parent.parent.left
                #case: when uncle is absent or black: 
                if(uncle == None) or (uncle.color == 'B'):
                    if(node == node.parent.right) and (node.parent != node.parent.parent.left):
                        if(node.parent.parent.parent == None):
                            if(root.right == node.parent):
                                tnode = self.LL(node.parent.parent)
                                tnode.parent = None
                                tnode.left.parent = tnode
                                color = tnode.color
                                tnode.color = tnode.left.color
                                tnode.left.color = color
                                root = tnode
                                return root
                        else:
                            if(node.parent.parent.parent.right == node.parent.parent):
                                tnode = self.LL(node.parent.parent)
                                node.parent.parent.parent.right = tnode
                            else:
                                tnode = self.LL(node.parent.parent)
                                node.parent.parent.parent.left = tnode
                    elif(node == node.parent.left):
                        if(node.parent.parent.parent.right == node.parent.parent):
                            tnode = self.LR(node.parent.parent)
                            node.parent.parent.parent.right = tnode 
                          
                        else:
                            tnode = self.LR(node.parent.parent)
                            node.parent.parent.parent.left = tnode
                    tnode.parent = node.parent.parent.parent
                    tnode.left.parent = tnode
                    tnode.right.parent = tnode
                    color = tnode.color
                    tnode.color = tnode.left.color
                    tnode.left.color = color
                    return root    
                elif(uncle != None) and (uncle.color == 'R'):
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    if(node.parent.parent.parent != None):
                        node.parent.parent.color = 'R'
                    node = node.parent.parent
        return root
                        
    def add_node(self,root,node) :
        if root is None: 
             return
        else: 
            if root.val < node.val: 
                if root.right is None: 
                    node.parent = root
                    root.right = node 
                else: 
                    self.add_node(root.right, node) 
            else: 
                if root.left is None:
                    node.parent = root
                    root.left = node 
                else: 
                    self.add_node(root.left, node)     
    
    def insert(self,root, val):
            if root is None:
                return Node(val,None,'B')
            else :
                node = Node(val,None,'R') 
                self.add_node(root,node)
                root = self.Balance(root,node)
            return root
        
def Search(root,key):
    if root is None:
        return 
    if(root.val == key):
        print('Element found !')
    if(root.val < key):
        Search(root.right,key)
    elif (root.val> key):
        Search(root.left,key)
        
def Preorder(root):
    if root is None:
        return
    print(root.val,'(',root.color,')', end = "  ")
    Preorder(root.left)
    Preorder(root.right)
        
def main():
    list = [1,2,3,4,5,6,7]
    rb_tree = RB_tree()
    root = None
    for i in list:
        root = rb_tree.insert(root,i)
    print('Preorder Traversal of RED BLACK TREE:')
    Preorder(root)
    x = int(input('\n Enter key to be searched:'))
    Search(root,x)


if __name__ == "__main__":
    main()
