def gnome_sort(data, key, direction = 'A'):

	# Start from beginning of data
	focusedIndex = 0
	while focusedIndex < len(data):
		if focusedIndex == 0:
			focusedIndex = focusedIndex + 1
		
		# Move towards end if prevous value smaller 
		# If previously moving element, stops and moves forward to next element
		if (direction == 'A' and data[focusedIndex][key] >= data[focusedIndex - 1][key]) or (direction == 'D' and data[focusedIndex][key] <= data[focusedIndex - 1][key]):
			focusedIndex = focusedIndex + 1

		# 'Bubble' value to start if previous value larger
		else:
			# Swap values
			data[focusedIndex], data[focusedIndex-1] = data[focusedIndex-1], data[focusedIndex]

			# Focused Index decreases to move element to start (where elements are smaller)
			focusedIndex = focusedIndex - 1

# Testing
if __name__ == "__main__":
    array = [{'Package': 'Golden Gate', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 227}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 2, 'Cost': 238}, {'Package': 'Special Number 3.', 'Customer': 'James Tay', 'Pax': 4, 'Cost': 198}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Alice Margatroid', 'Pax': 2, 'Cost': 150}, {'Package': 'Furry Friends', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 288}, {'Package': 'Australia.', 'Customer': 'Elon Musk', 'Pax': 5, 'Cost': 273}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'John Lim', 'Pax': 1, 'Cost': 164}, {'Package': 'Honeymoon Suite', 'Customer': 'Lancelot R. Gilligrass', 'Pax': 3, 'Cost': 393}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 5, 'Cost': 269}, {'Package': 'Fun with Family', 'Customer': 'Alice Margatroid', 'Pax': 5, 'Cost': 271}]
    gnome_sort(array, 'Pax', 'D')
    for n in array:
        print(n['Pax'])