def insertion_sort(array, key, direction = "A"):

    # Elements are 're-inserted' back into the array based on the 'new' elements.

    # Move the index of an element according to the elements on its left.
    # Moved with reversed bubble sort, to the start of the array.
    
    # First element is skipped; no element to its left.
    for index in range(1, len(array)):

        # Index, value of element to be moved
        focusedIndex = index
        focusedElement = array[index]


        while focusedIndex > 0 and ((direction == "A" and focusedElement[key] < array[focusedIndex - 1][key]) or (direction == "D" and focusedElement[key] > array[focusedIndex - 1][key])):
            # index > 0 to prevent Index Error

            # If value to the left is greater, insert into the index.
            # *Values can be also be inserted at index[0]
            array[focusedIndex] = array[focusedIndex - 1]
            array[focusedIndex - 1] = focusedElement

            # Check against the leftward element next loop
            focusedIndex -= 1

# Testing
if __name__ == "__main__":
    array = [{'Package': 'Golden Gate', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 227}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 2, 'Cost': 238}, {'Package': 'Special Number 3.', 'Customer': 'James Tay', 'Pax': 4, 'Cost': 198}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Alice Margatroid', 'Pax': 2, 'Cost': 150}, {'Package': 'Furry Friends', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 288}, {'Package': 'Australia.', 'Customer': 'Elon Musk', 'Pax': 5, 'Cost': 273}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'John Lim', 'Pax': 1, 'Cost': 164}, {'Package': 'Honeymoon Suite', 'Customer': 'Lancelot R. Gilligrass', 'Pax': 3, 'Cost': 393}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 5, 'Cost': 269}, {'Package': 'Fun with Family', 'Customer': 'Alice Margatroid', 'Pax': 5, 'Cost': 271}]
    insertion_sort(array, 'Package', 'D')
    for n in array:
        print(n['Package'])