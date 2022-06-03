# The storage class for creating binary tree nodes 

class Node: 
    def __init__(self, data): 
        # List for duplicate elements
        self.data = [data] 
        self.left = None 
        self.right = None 
 
 
# Implementation of the Binary Search Tree 
class BinarySearchTree: 
 
    # Creates an initially empty BST 
    def __init__(self): 
        self._root = None 
        self._size = 0 
 
    # Returns the total number of elements in the BST 
    def __len__(self): 
        return self._size

    # Insert new_node into the BST 
    def insertNode(self, new_node, key, direction = "A"): 
        self._size += 1
        if self._root is None: 
            self._root = new_node
        else: 
            self._recInsertNode(self._root, new_node, key, direction) 
 
 
    # Helper method to insert new_node into the BST recursively from start_node 
    def _recInsertNode(self, start_node, new_node, key, direction):
        # Check first value, since all are same
        if (direction == "A" and start_node.data[0][key] < new_node.data[0][key]) or (direction == "D" and start_node.data[0][key] > new_node.data[0][key]): 
            if start_node.right is None: 
                start_node.right = new_node
            else: 
                self._recInsertNode(start_node.right, new_node, key, direction) 
        elif (direction == "A" and start_node.data[0][key] > new_node.data[0][key]) or (direction == "D" and start_node.data[0][key] < new_node.data[0][key]):
            if start_node.left is None: 
                start_node.left = new_node
            else:
                self._recInsertNode(start_node.left, new_node, key, direction)
        else:
            # Same value, add to tree as same value
            if len(start_node.data) != 0:
                start_node.data.append(new_node.data[0])





    
    # In-order traversal of the BST 
    def inorderTrav(self, array): 
        if self._root is None: 
            print("Tree is empty!") 
        else:
            # Use pre order recursive
            self._recInorderTrav(self._root, array)

    # Helper method to perform In-order Traversal of the given subtree recursively 
    def _recInorderTrav(self, subtree, array):
        if subtree.left != None:
            self._recInorderTrav(subtree.left, array)

        # Add traversed values back
        for data in subtree.data:
            array.append(data)

        if subtree.right != None:
            self._recInorderTrav(subtree.right, array)


def tree_sort(array, key, direction = "A"):
    binary_tree = BinarySearchTree()
    while array != []:
        # Remove from list, into binary tree
        binary_tree.insertNode(Node(array.pop()), key, direction)
    binary_tree.inorderTrav(array)

# Testing
if __name__ == "__main__":
    array = [{'Package': 'Golden Gate', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 227}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 2, 'Cost': 238}, {'Package': 'Special Number 3.', 'Customer': 'James Tay', 'Pax': 4, 'Cost': 198}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Alice Margatroid', 'Pax': 2, 'Cost': 150}, {'Package': 'Furry Friends', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 288}, {'Package': 'Australia.', 'Customer': 'Elon Musk', 'Pax': 5, 'Cost': 273}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'John Lim', 'Pax': 1, 'Cost': 164}, {'Package': 'Honeymoon Suite', 'Customer': 'Lancelot R. Gilligrass', 'Pax': 3, 'Cost': 393}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 5, 'Cost': 269}, {'Package': 'Fun with Family', 'Customer': 'Alice Margatroid', 'Pax': 5, 'Cost': 271}]
    tree_sort(array, 'Pax', "D")
    for n in array:
        print(n['Pax'])