from collections import deque as queue
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def findDepth(node):
    #initialising
    a = 0
    while (node != None):
        a += 1
        node = node.left
    return a


def isperf(root, a, level = 0):

    if (root == None):
        return True

    if (root.left == None and root.right == None):
        return (a == level + 1)

    if (root.left == None or root.right == None):
        return False

    return (isperf(root.left, a, level + 1) and
            isperf(root.right, a, level + 1))


def isbinarytree(root):
    a = findDepth(root)
    return isperf(root, a)


def printLevelorder(root):
 
    if (root == None):
        return
 
    # Create an empty queue for
    # level order traversal
    q = queue()
 
    # To store front element of
    # queue.
    #node *curr
 
    # Enqueue Root and None node.
    q.append(root)
    q.append(None)
 
    while (len(q) > 1):
        curr = q.popleft()
        # q.pop()
 
        # Condition to check
        # occurrence of next
        # level.
        if (curr == None):
            q.append(None)
            print()
 
        else:
 
            # Pushing left child of
            # current node.
            if (curr.left):
                q.append(curr.left)
 
            # Pushing right child of
            # current node.
            if (curr.right):
                q.append(curr.right)
 
            print(curr.val, end=" ")


def printInorder(root):

    if root:

        #left child
        printInorder(root.left)

        #print
        print(root.val),

        #right child
        printInorder(root.right)

        
        
def printPreorder(root):
 
    if root:
 
        # print
        print(root.val),
 
        #left child
        printPreorder(root.left)
 
        #right child
        printPreorder(root.right)
        
        
        
def printPostorder(root):
 
    if root:
 
        #left child
        printPostorder(root.left)
 
        #right child
        printPostorder(root.right)
 
        #print
        print(root.val)
 


if __name__ == "__main__":
    
    n=int(input("Enter the number of nodes(between 5 and 7) : "))
    if(n==5):
        print("Enter",n," nodes of a binary tree : ")
        a=int(input("Enter the root node : "))
        b=int(input("Enter node to the left of root node : "))
        c=int(input("Enter node to the right of root node : "))
        d=int(input("Enter node to the left of left node : "))
        e=int(input("Enter node to the right of left node : "))
        root = Node(a)
        root.left = Node(b)
        root.right = Node(c)
        root.left.left = Node(d)
        root.left.right = Node(e)
        print("        ",a,"          ")    
        print("       /   \            ")
        print("     ",b,"   ",c,"            ")
        print("     / \     ")
        print("   ",d," ",e,"    ")
        print()
        if (isbinarytree(root)):
            print("Yes,this is a perfect binary tree")
        else:
            print("No,this is not a perfect binary tree")
    
    
    elif(n==6):
        print("Enter",n," nodes of a binary tree : ")
        a=int(input("Enter the root node : "))
        b=int(input("Enter node to the left of root node : "))
        c=int(input("Enter node to the right of root node : "))
        d=int(input("Enter node to the left of left node : "))
        e=int(input("Enter node to the right of left node : "))
        f=int(input("Enter node to the left of right node : "))
        root = Node(a)
        root.left = Node(b)
        root.right = Node(c)
        root.left.left = Node(d)
        root.left.right = Node(e)
        root.right.left = Node(f)
        print()
        print("        ",a,"          ")    
        print("       /   \            ")
        print("     ",b,"   ",c,"            ")
        print("     / \     /")
        print("   ",d," ",e,"",f)
        print()
        if (isbinarytree(root)):
            print("Yes,this is a perfect binary tree")
        else:
            print("No,this is not a perfect binary tree")
    
    
    else:
        print("Enter",n," nodes of a binary tree : ")
        a=int(input("Enter the root node : "))
        b=int(input("Enter node to the left of root node : "))
        c=int(input("Enter node to the right of root node : "))
        d=int(input("Enter node to the left of left node : "))
        e=int(input("Enter node to the right of left node : "))
        f=int(input("Enter node to the left of right node : "))
        g=int(input("Enter node to the right of right node : "))
    
        root = Node(a)
        root.left = Node(b)
        root.right = Node(c)
        root.left.left = Node(d)
        root.left.right = Node(e)
        root.right.left=Node(f)
        root.right.right=Node(g)
        print()
        print("        ",a,"          ")    
        print("       /    \            ")
        print("     ",b,"    ",c,"            ")
        print("     / \    / \ ")
        print("   ",d," ",e,"",f," ",g)
        print()
        if (isbinarytree(root)):
            print("Yes,this is a perfect binary tree")
        else:
            print("No,this is not a perfect binary tree")

            
print()
print()
print("1.Inorder traversal , 2.Preorder traversal , 3.Postorder traversal , 4.Level Order traversal , 5.All traversals")
choice=int(input("Enter your choice : "))
if(choice==1):
    print ("In-order traversal of binary tree is")
    printInorder(root)
elif(choice==2):
    print ("Pre-order traversal of binary tree is")
    printPreorder(root)
elif(choice==3):
    print ("Post-order traversal of binary tree is")
    printPostorder(root)
elif(choice==4):
    print("Level order traversal of binary tree is")
    printLevelorder(root)
elif(choice==5):
    print ("In-order traversal of the tree is")
    printInorder(root)
    print ("Pre-order traversal of the tree is")
    printPreorder(root)
    print ("Post-order traversal of the tree is")
    printPostorder(root)
    print("Level order traversal of the tree is")
    printLevelorder(root)
else:
    print()
    print("Invalid choice")