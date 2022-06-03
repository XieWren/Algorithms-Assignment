# The storage class for creating binary tree nodes 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 
 
 
# Implementation of the Binary Search Tree 
class BinarySearchTree: 
 
    # Creates an initially empty BST 
    def __init__(self): 
        self.root = None 
        self.size = 0 
 
    # Returns the total number of elements in the BST 
    def __len__(self): 
        return self.size

    # Insert new_node into the BST 
    def insertNode(self, new_node): 
        self.size += 1
        if self.root is None: 
            self.root = new_node
        else: 
            self.recInsertNode(self.root, new_node) 
 
 
    # Helper method to insert new_node into the BST recursively from start_node 
    def recInsertNode(self, start_node, new_node):
        if start_node.data < new_node.data: 
            if start_node.right is None: 
                start_node.right = new_node
            else: 
                self.recInsertNode(start_node.right, new_node) 
        else: 
            if start_node.left is None: 
                start_node.left = new_node
            else:
                self.recInsertNode(start_node.left, new_node)



    
    # In-order traversal of the BST 
    def inorderTrav(self): 
        if self.root is None: 
            print("Tree is empty!") 
        else:
            # Use pre order recursive
            self.recInorderTrav(self.root) 
    
    # Helper method to perform In-order Traversal of the given subtree recursively 
    def recInorderTrav(self, subtree):
        if subtree.left != None:
            self.recInorderTrav(subtree.left)

        print(subtree.data, end=" ")

        if subtree.right != None:
            self.recInorderTrav(subtree.right)


# Test code 
if __name__ == '__main__': 
    bst = BinarySearchTree() 

    nodes = [60, 12, 90, 4, 41, 1, 100, 71, 29, 37, 84, 23]
    
    for node in nodes:
        bst.insertNode(Node(node))
 
    print("Size of BST: ", len(bst)) 
 

    print("\n\nIn-order Traversal of BST:") 
    print("===========================") 
    bst.inorderTrav() 