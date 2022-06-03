def selection_sort(array, key, direction = "A"):
    # No. of Passes Required = (No. of Elements) - 1
    # Because the last swap will fix 2 elements at once!

    for currentIndex in range(len(array)-1):
        
        # Focus on moving the smallest values to the start of the array.
        # Specific selection of nth-smallest value to swap to nth-smallest index position.

        smallerIndex = currentIndex

        # Range of comparing indexes decrease per pass.
        # Previous nth-smallest value no longer needs to be moved.
        for comparingIndex in range(currentIndex, len(array)):
            # Check for nth-smallest value in array.
            if (direction == "A" and array[comparingIndex][key] < array[smallerIndex][key]) or (direction == "D" and array[comparingIndex][key] > array[smallerIndex][key]):
                smallerIndex = comparingIndex

        # Selectively swap elements
        temp = array[currentIndex]
        array[currentIndex] = array[smallerIndex]
        array[smallerIndex] = temp

# Testing
if __name__ == "__main__":
    array = [{'Package': 'Golden Gate', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 227}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 2, 'Cost': 238}, {'Package': 'Special Number 3.', 'Customer': 'James Tay', 'Pax': 4, 'Cost': 198}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Alice Margatroid', 'Pax': 2, 'Cost': 150}, {'Package': 'Furry Friends', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 288}, {'Package': 'Australia.', 'Customer': 'Elon Musk', 'Pax': 5, 'Cost': 273}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'John Lim', 'Pax': 1, 'Cost': 164}, {'Package': 'Honeymoon Suite', 'Customer': 'Lancelot R. Gilligrass', 'Pax': 3, 'Cost': 393}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 5, 'Cost': 269}, {'Package': 'Fun with Family', 'Customer': 'Alice Margatroid', 'Pax': 5, 'Cost': 271}]
    selection_sort(array, 'Pax', 'D')
    for n in array:
        print(n['Pax'])