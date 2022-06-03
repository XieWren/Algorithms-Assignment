def gnomeSort(array):

	# Start from beginning of array
	focusedIndex = 0
	while focusedIndex < len(array):

		# Increment forward; allow for checking with previous element
		if focusedIndex == 0:
			focusedIndex = focusedIndex + 1
		
		# Move towards end if prevous value smaller 
		# If previously moving element, stops and moves forward to next element
		if array[focusedIndex] >= array[focusedIndex - 1]:
			focusedIndex = focusedIndex + 1

		# 'Bubble' value to start if previous value larger
		else:
			# Swap values
			array[focusedIndex], array[focusedIndex-1] = array[focusedIndex-1], array[focusedIndex]

			# Focused Index decreases to move element to start (where elements are smaller)
			focusedIndex = focusedIndex - 1
			print(array)

	return array


array = [60, 12, 90, 4, 41, 1, 100, 71, 29, 37, 84, 23]
array = gnomeSort(array)
print(array)

"""

4:
[12, 60, 90, 4, 41, 1, 100, 71, 29, 37, 84, 23]
[12, 60, 4, 90, 41, 1, 100, 71, 29, 37, 84, 23]
[12, 4, 60, 90, 41, 1, 100, 71, 29, 37, 84, 23]
[4, 12, 60, 90, 41, 1, 100, 71, 29, 37, 84, 23]

12:
[4, 12, 60, 41, 90, 1, 100, 71, 29, 37, 84, 23]

1:
[4, 12, 41, 60, 90, 1, 100, 71, 29, 37, 84, 23]
[4, 12, 41, 60, 1, 90, 100, 71, 29, 37, 84, 23]
[4, 12, 41, 1, 60, 90, 100, 71, 29, 37, 84, 23]
[4, 12, 1, 41, 60, 90, 100, 71, 29, 37, 84, 23]
[4, 1, 12, 41, 60, 90, 100, 71, 29, 37, 84, 23]
[1, 4, 12, 41, 60, 90, 100, 71, 29, 37, 84, 23]


[1, 4, 12, 41, 60, 90, 71, 100, 29, 37, 84, 23]
[1, 4, 12, 41, 60, 71, 90, 100, 29, 37, 84, 23]
[1, 4, 12, 41, 60, 71, 90, 29, 100, 37, 84, 23]
[1, 4, 12, 41, 60, 71, 29, 90, 100, 37, 84, 23]
[1, 4, 12, 41, 60, 29, 71, 90, 100, 37, 84, 23]
[1, 4, 12, 41, 29, 60, 71, 90, 100, 37, 84, 23]
[1, 4, 12, 29, 41, 60, 71, 90, 100, 37, 84, 23]
[1, 4, 12, 29, 41, 60, 71, 90, 37, 100, 84, 23]
[1, 4, 12, 29, 41, 60, 71, 37, 90, 100, 84, 23]
[1, 4, 12, 29, 41, 60, 37, 71, 90, 100, 84, 23]
[1, 4, 12, 29, 41, 37, 60, 71, 90, 100, 84, 23]
[1, 4, 12, 29, 37, 41, 60, 71, 90, 100, 84, 23]
[1, 4, 12, 29, 37, 41, 60, 71, 90, 84, 100, 23]
[1, 4, 12, 29, 37, 41, 60, 71, 84, 90, 100, 23]
[1, 4, 12, 29, 37, 41, 60, 71, 84, 90, 23, 100]
[1, 4, 12, 29, 37, 41, 60, 71, 84, 23, 90, 100]
[1, 4, 12, 29, 37, 41, 60, 71, 23, 84, 90, 100]
[1, 4, 12, 29, 37, 41, 60, 23, 71, 84, 90, 100]
[1, 4, 12, 29, 37, 41, 23, 60, 71, 84, 90, 100]
[1, 4, 12, 29, 37, 23, 41, 60, 71, 84, 90, 100]
[1, 4, 12, 29, 23, 37, 41, 60, 71, 84, 90, 100]
[1, 4, 12, 23, 29, 37, 41, 60, 71, 84, 90, 100]
[1, 4, 12, 23, 29, 37, 41, 60, 71, 84, 90, 100]

"""