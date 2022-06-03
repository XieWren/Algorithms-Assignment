def cocktail_shaker_sort(array, key, direction = 'A'):

    # No. of Passes Required = (No. of Elements) - 1
    # Because the last swap will fix 2 elements at once!

    for passes in range(len(array) - 1, 0, -1):
        sorting = False

        # Bubble small values to beginning or array        
        for focusedIndex in range(passes, 0, -1):

            # Check against adjacent elements, to continually bubble the smaller element
            currentElement = array[focusedIndex]
            comparingElement = array[focusedIndex - 1]

            if (direction == "A" and comparingElement[key] > currentElement[key]) or (direction == "D" and comparingElement[key] < currentElement[key]):

                # Swap elements if any two adjacent elements are out of order.
                array[focusedIndex] = currentElement
                array[focusedIndex-1] = comparingElement
                
                sorting = True

        # Switch; bubble large values to beginning of array
        for focusedIndex in range(passes):

            # Check against adjacent elements, to continually bubble the larger element
            currentElement = array[focusedIndex]
            comparingElement = array[focusedIndex + 1]

            if (direction == "A" and comparingElement[key] < currentElement[key]) or (direction == "D" and comparingElement[key] > currentElement[key]):
                
                # Swap elements if any two adjacent elements are out of order.
                array[focusedIndex] = comparingElement
                array[focusedIndex + 1] = currentElement

                sorting = True
        
        # Stops sorting if already sorted
        if not sorting:
            return
 
# Testing
if __name__ == "__main__":
    array = [{'Package': 'Golden Gate', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 227}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 2, 'Cost': 238}, {'Package': 'Special Number 3.', 'Customer': 'James Tay', 'Pax': 4, 'Cost': 198}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Alice Margatroid', 'Pax': 2, 'Cost': 150}, {'Package': 'Furry Friends', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 288}, {'Package': 'Australia.', 'Customer': 'Elon Musk', 'Pax': 5, 'Cost': 273}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'John Lim', 'Pax': 1, 'Cost': 164}, {'Package': 'Honeymoon Suite', 'Customer': 'Lancelot R. Gilligrass', 'Pax': 3, 'Cost': 393}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 5, 'Cost': 269}, {'Package': 'Fun with Family', 'Customer': 'Alice Margatroid', 'Pax': 5, 'Cost': 271}]
    cocktail_shaker_sort(array, 'Pax', 'D')
    for n in array:
        print(n['Pax'])