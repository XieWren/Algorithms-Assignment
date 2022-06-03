def bubble_sort(array, key, direction = "A"):
    
    # No. of Passes Required = (No. of Elements) - 1
    # Because the last swap will fix 2 elements at once!

    sorted = False

    for passes in range(len(array)-1, 0, -1):
        
        # Stop if already sorted
        if sorted:
            break

        sorted = True

        # Focus on moving the largest values to the end of the array.
        # 'Bubbling' them to the end of the array.

        # focusedIndex refers to moving the value to the index with the nth-largest value.
        # This value decreases per pass, as the previous nth-largest value no longer needs to be moved.

        for focusedIndex in range(passes):
            
            # Check against adjacent elements, to continually bubble the larger element
            currentElement = array[focusedIndex]
            comparingElement = array[focusedIndex+1]
            
            # Swap elements if any two adjacent elements are out of order.
            if (direction == "A" and currentElement[key] > comparingElement[key]) or (direction == "D" and currentElement[key] < comparingElement[key]):
                sorted = False
                array[focusedIndex] = comparingElement
                array[focusedIndex+1] = currentElement

# Testing
if __name__ == "__main__":
    from time import time
    
    array = [{'Package': 'Golden Gate', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 227}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 2, 'Cost': 238}, {'Package': 'Special Number 3.', 'Customer': 'James Tay', 'Pax': 4, 'Cost': 198}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Alice Margatroid', 'Pax': 2, 'Cost': 150}, {'Package': 'Furry Friends', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 288}, {'Package': 'Australia.', 'Customer': 'Elon Musk', 'Pax': 5, 'Cost': 273}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'John Lim', 'Pax': 1, 'Cost': 164}, {'Package': 'Honeymoon Suite', 'Customer': 'Lancelot R. Gilligrass', 'Pax': 3, 'Cost': 393}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 5, 'Cost': 269}, {'Package': 'Fun with Family', 'Customer': 'Alice Margatroid', 'Pax': 5, 'Cost': 271}]
    now = time()
    bubble_sort(array, 'Pax', 'D')
    print("Time:", time() - now)
    for n in array:
        print(n['Pax'])