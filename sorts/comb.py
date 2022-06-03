def comb_sort(array, key, direction = 'A'):

    gap = len(array)
    swaps = True

    while gap > 1 or swaps:
        # Minimum gap is 1
        # Start with huge gap to quickly move elements closer together, then start checking more thoroughly.
        gap = max(1, int(gap / 1.25))
        
        swaps = False
        
        # Each gap temporarily increments index; ensure no index error.
        for focusedIndex in range(len(array) - gap):

            # Compare with elements across a gap; move elements close together faster.
            comparingIndex = focusedIndex + gap

            # Swap if out of place
            if (direction == "A" and array[focusedIndex][key] > array[comparingIndex][key]) or (direction == "D" and array[focusedIndex][key] < array[comparingIndex][key]):
                array[focusedIndex], array[comparingIndex] = array[comparingIndex], array[focusedIndex]
                swaps = True
 
# Testing
if __name__ == "__main__":
    array = [{'Package': 'Golden Gate', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 227}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 2, 'Cost': 238}, {'Package': 'Special Number 3.', 'Customer': 'James Tay', 'Pax': 4, 'Cost': 198}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Alice Margatroid', 'Pax': 2, 'Cost': 150}, {'Package': 'Furry Friends', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 288}, {'Package': 'Australia.', 'Customer': 'Elon Musk', 'Pax': 5, 'Cost': 273}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'John Lim', 'Pax': 1, 'Cost': 164}, {'Package': 'Honeymoon Suite', 'Customer': 'Lancelot R. Gilligrass', 'Pax': 3, 'Cost': 393}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 5, 'Cost': 269}, {'Package': 'Fun with Family', 'Customer': 'Alice Margatroid', 'Pax': 5, 'Cost': 271}]
    comb_sort(array, 'Pax', 'D')
    for n in array:
        print(n['Pax'])