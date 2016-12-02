class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
 
 
def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)

def inOrder(tree):
        stack = []      
        currentNode = tree      #current node of the tree
        while True:     #the loop will always run until it has gone through the entire tree
            while currentNode != None: #until the node is not equal to node it will append the value of the current to the stack
                stack.append(currentNode) 
                currentNode = currentNode.left #moves to the left side of the tree
            if len(stack) == 0:  #when the length of the stack is 0 it has traversed the entire tree and breaks out of the loop
                break
            currentNode = stack.pop()       #pops the value that is at the top of the stack, also backtracks through the stack
            print (currentNode.value)
            currentNode = currentNode.right     #sets the node to go to the right
            
                
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
  print("--------")
  inOrder(t)



