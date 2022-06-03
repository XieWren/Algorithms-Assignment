def combSort(array):

    gap = len(array)
    swaps = True

    while gap > 1 or swaps:
        print(gap)
        print(array)
        # Minimum gap is 1
        # Start with huge gap to quickly move elements closer together, then start checking more thoroughly.
        gap = max(1, int(gap / 1.25))
        
        swaps = False
        
        # Each gap temporarily increments index; ensure no index error.
        for focusedIndex in range(len(array) - gap):

            # Compare with elements across a gap; move elements close together faster.
            comparingIndex = focusedIndex + gap

            # Swap if out of place
            if array[focusedIndex] > array[comparingIndex]:
                array[focusedIndex], array[comparingIndex] = array[comparingIndex], array[focusedIndex]
                swaps = True
 
array = [75, 16, 55, 19, 48, 14, 2, 61, 22, 100]

print("Before:", array)
combSort(array)
print("After: ", array)


"""

 Elements being compared:
 ┏━━━━┓ 
 
 Move forward to next index [Iterative]:
 —→

Sort 1: Gap = 8
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ —→
[75, 16, 55, 19, 48, 14, 2, 61, 22, 100]

Sort 2: Gap = 6
 ┏━━━━━━━━━━━━━━━━━━━━━━━┓ —→
[22, 16, 55, 19, 48, 14, 2, 61, 75, 100]

Sort 3: Gap = 4
 ┏━━━━━━━━━━━━━━━━┓ —→
[2, 16, 55, 19, 48, 14, 22, 61, 75, 100]

Sort 4: Gap = 3
 ┏━━━━━━━━━━━━┓ —→
[2, 14, 22, 19, 48, 16, 55, 61, 75, 100]

Sort 5: Gap = 2
 ┏━━━━━━━━┓ —→
[2, 14, 16, 19, 48, 22, 55, 61, 75, 100]

Sort 6: Gap = 1
 ┏━━━━┓ —→
[2, 14, 16, 19, 48, 22, 55, 61, 75, 100]

Result:
[2, 14, 16, 19, 22, 48, 55, 61, 75, 100]

"""