def cocktail_shaker_sort(array):

    # No. of Passes Required = (No. of Elements) - 1
    # Because the last swap will fix 2 elements at once!

    for passes in range(len(array) - 1, 0, -1):
        sorting = False

        # Bubble small values to beginning or array        
        for focusedIndex in range(passes, 0, -1):

            # Check against adjacent elements, to continually bubble the smaller element
            currentElement = array[focusedIndex]
            comparingElement = array[focusedIndex - 1]

            if comparingElement > currentElement:

                # Swap elements if any two adjacent elements are out of order.
                array[focusedIndex] = currentElement
                array[focusedIndex-1] = comparingElement
                
                sorting = True

        # Switch; bubble large values to beginning of array
        for focusedIndex in range(passes):

            # Check against adjacent elements, to continually bubble the larger element
            currentElement = array[focusedIndex]
            comparingElement = array[focusedIndex + 1]

            if currentElement > comparingElement:
                
                # Swap elements if any two adjacent elements are out of order.
                array[focusedIndex] = comparingElement
                array[focusedIndex + 1] = currentElement

                sorting = True
        
        # Stops sorting if already sorted
        if not sorting:
            return array
 

array = [60, 12, 90, 4, 41, 1, 100, 71, 29, 37, 84, 23]
print(cocktail_shaker_sort(array))