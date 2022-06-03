def heap_sort(array, key, direction = "A"):
    length = len(array)

    # Create max heap from unsorted array
    # A max heap is an ordered binary tree where all parent > child
    for focusedIndex in range(length//2, -1, -1):
        heapify(array, length, focusedIndex, key, direction)

    # Working range decreases
    for workingRange in range(length-1, 0, -1):
        # Swap root element (currently swappingIndex value) with last element of working range
        array[workingRange], array[0] = array[0], array[workingRange]

        # Heapify again, but only compare & swap root element [index 0]
        heapify(array, workingRange, 0, key, direction)

# focusedIndex functions as parent node, is swapped with child nodes so that parent node > child node.
# Used to create a max heap.
def heapify(array, length, focusedIndex, key, direction):
    
    # Find swappingIndex value in tree (root and children included)
    swappingIndex = focusedIndex
    leftIndex = 2 * focusedIndex + 1
    rightIndex = 2 * focusedIndex + 2

    # print("Left:", leftIndex, "Right:", rightIndex, "Focused:" , focusedIndex)

    # Compare parent node (focusedIndex) against child nodes (leftIndex, rightIndex)

    # Only compare with elements in working range
    if leftIndex < length:
        # Ascending
        if direction == "A" and array[focusedIndex][key] < array[leftIndex][key]:
            swappingIndex = leftIndex
        # Descending
        elif direction == "D" and array[focusedIndex][key] > array[leftIndex][key]:
            swappingIndex = leftIndex

    if rightIndex < length:
        # Ascending
        if direction == "A" and array[swappingIndex][key] < array[rightIndex][key]:
            swappingIndex = rightIndex
        #Descending
        elif direction == "D" and array[swappingIndex][key] > array[rightIndex][key]:
            swappingIndex = rightIndex

    # Larger value (if exists) is taken, and swapped with the parent node.
    if swappingIndex != focusedIndex:
        array[focusedIndex], array[swappingIndex] = array[swappingIndex], array[focusedIndex]

        # Old node is compared with child nodes further down, to determine whether swap is needed.
        heapify(array, length, swappingIndex, key, direction)

# Testing
if __name__ == "__main__":
    array = [{'Package': 'Golden Gate', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 227}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 2, 'Cost': 238}, {'Package': 'Special Number 3.', 'Customer': 'James Tay', 'Pax': 4, 'Cost': 198}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Alice Margatroid', 'Pax': 2, 'Cost': 150}, {'Package': 'Furry Friends', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 288}, {'Package': 'Australia.', 'Customer': 'Elon Musk', 'Pax': 5, 'Cost': 273}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'John Lim', 'Pax': 1, 'Cost': 164}, {'Package': 'Honeymoon Suite', 'Customer': 'Lancelot R. Gilligrass', 'Pax': 3, 'Cost': 393}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 5, 'Cost': 269}, {'Package': 'Fun with Family', 'Customer': 'Alice Margatroid', 'Pax': 5, 'Cost': 271}]
    heap_sort(array, 'Pax', 'D')
    for n in array:
        print(n['Pax'])


"""
Part 1: Create Max Heap
    
         100
     /         \
    84          90
   /  \        /  \
  71   41     23   60
 / \   / \   /
4  29 37 12 1

Part 2: Swap root element with last element
          1
     /         \
    84          90
   /  \        /  \
  71   41     23   60
 / \   / \   /
4  29 37 12 100

Part 3: Remove last element from tree (permanent index in array)
          1
     /         \
    84          90
   /  \        /  \
  71   41     23   60
 / \   / \ 
4  29 37 12

Part 4: Heapify root element to ensure max heap is maintained

          90
     /         \
    84          1
   /  \        /  \
  71   41     23   60
 / \   / \ 
4  29 37 12

          90
     /         \
    84          60
   /  \        /  \
  71   41     23   1
 / \   / \ 
4  29 37 12

"""