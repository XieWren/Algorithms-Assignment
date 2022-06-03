def heapSort(array):
    length = len(array)

    # Create max heap from unsorted array
    # A max heap is an ordered binary tree where all parent > child
    for focusedIndex in range(length//2, -1, -1):
        heapify(array, length, focusedIndex)

    # Working range decreases
    for workingRange in range(length-1, 0, -1):
        # Swap root element (currently largest value) with last element of working range
        array[workingRange], array[0] = array[0], array[workingRange]

        # Heapify again, but only compare & swap root element [index 0]
        heapify(array, workingRange, 0)

# focusedIndex functions as parent node, is swapped with child nodes so that parent node > child node.
# Used to create a max heap.
def heapify(array, length, focusedIndex):

    # Find largest value in tree (root and children included)
    largest = focusedIndex
    leftIndex = 2 * focusedIndex + 1
    rightIndex = 2 * focusedIndex + 2

    # print("Left:", leftIndex, "Right:", rightIndex, "Focused:" , focusedIndex)

    # Compare parent node (focusedIndex) against child nodes (leftIndex, rightIndex)

    # Only compare with elements in working range; 
    if leftIndex < length and array[focusedIndex] < array[leftIndex]:
        largest = leftIndex


    if rightIndex < length and array[largest] < array[rightIndex]:
        largest = rightIndex

    # Larger value (if exists) is taken, and swapped with the parent node.
    if largest != focusedIndex:
        array[focusedIndex], array[largest] = array[largest], array[focusedIndex]

        # Old node is compared with child nodes further down, to determine whether swap is needed.
        heapify(array, length, largest)
  
array = [60, 12, 90, 4, 41, 1, 100, 71, 29, 37, 84, 23]
print('Before:', array)
heapSort(array)
print('After:', array)


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