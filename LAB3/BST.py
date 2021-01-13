# Python program for reading from file
file = open('numbers.txt', 'r')

# Reading from the file
content = file.readlines()

# Array for storing
array = []
# Iterating through the content
for line in content:
    array.append(line.rstrip())
    # print(array)


# A Binary tree node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self, root):
        self.root = root

    def insertNode(self, value):
        new_node = Node(value)
        # the new element will become the head
        if self.root is None:
            self.root = new_node
        else:
            x = self.root
            temp = None
            while x is not None:
                temp = x
                if value < x.key:
                    x = x.left
                else:
                    x = x.right
            new_node.parent = temp
            if value > temp.key:
                temp.right = new_node
            else:
                temp.left = new_node

    def searchNode(self, x, searchValue):
        # Base Cases: root is null or key is present at root
        if x is None or int(x.key) == searchValue:
            return x
        # Key is greater than root's key
        if int(x.key) < searchValue:
            return theTree.searchNode(x.right, searchValue)
        # Key is smaller than root's key
        else:
            return theTree.searchNode(x.left, searchValue)

    # Program to find minimum depth of a given Binary Tree
    def minDepth(self, root):
        # Corner Case Should never be hit unless the code is called on root = NULL
        if root.key is None:
            return 0

        # Base Case : Leaf node.This acoounts for height = 1
        if root.left is None and root.right is None:
            return 1

        # If left subtree is Null, recur for right subtree
        if root.left is None:
            return self.minDepth(root.right) + 1

        # If right subtree is Null , recur for left subtree
        if root.right is None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # Program to find minimum depth of a given Binary Tree
    def maxDepth(self, root):
        # Corner Case Should never be hit unless the code is called on root = NULL
        if root is None:
            return 0

        # Base Case : Leaf node.This acoounts for height = 1
        if root.left is None and root.right is None:
            return 1

        # If left subtree is Null, recur for right subtree
        if root.left is None:
            return self.maxDepth(root.right) + 1

        # If right subtree is Null , recur for left subtree
        if root.right is None:
            return self.maxDepth(root.left) + 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # A recursive python program to find LCA of two nodes n1 and n2

    # Function to find LCA of n1 and n2. The function assumes that both n1 and n2 are present in BST
    def lca(self, root, n1, n2):

        # Base Case
        if root is None:
            return None

        # If both n1 and n2 are smaller than root, then LCA lies in left
        if int(root.key) > n1 and int(root.key) > n2:
            return self.lca(root.left, n1, n2)

        # If both n1 and n2 are greater than root, then LCA lies in right
        if int(root.key) < n1 and int(root.key) < n2:
            return self.lca(root.right, n1, n2)

        return root

    def printTree(self, someNode):
        if someNode is None:
            pass
        else:
            self.printTree(someNode.left)
            print(someNode.key)
            self.printTree(someNode.right)


# Driver program to test above function

# create empty tree with None as root
theTree = BST(None)

# Construct the bst from the file values
for i in range(0, len(array)):
    theTree.insertNode(array[i])

minD = theTree.minDepth(theTree.root)
print("min depth: ", minD)

maxD = theTree.maxDepth(theTree.root)
print("max depth: ", maxD)

print("printing in in-order")
theTree.printTree(theTree.root)

print("Input 2 numbers from the above tree to find their lowest common ancestor")
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
t = theTree.lca(theTree.root, n1, n2)
print("LCA of ", n1, " and ", n2, " is ", t.key)


# print("Input 2 numbers to find their lowest common ancestor")
# k=0
# while(k==0):
#     n1 = int(input("First number: "))
#     f = theTree.searchNode(theTree.root, n1)
#     n2 = int(input("Second number: "))
#     f = theTree.searchNode(theTree.root, n1)
#     if n1 == True and n2 == True:
#         t = theTree.lca(theTree.root, n1, n2)
#         print("LCA of ", n1, " and ", n2, " is ", t.key)
#         k=1
#     # else:
#         n1 = int(input("First number: "))
#         f = theTree.searchNode(theTree.root, n1)
#         n2 = int(input("Second number: "))
#         f = theTree.searchNode(theTree.root, n1)
