from random import shuffle
from time import sleep

def bogosort(array):

    sorting = True
    count = 0

    while sorting:

        sorting = False
        
        # Check if sorted
        if len(array) > 1:
            # Compare each element to the next, 
            for index in range(len(array) - 1):

                # Plan to 'sort' if unsorted
                if array[index] > array[index + 1]:
                    sorting = True
                    break
        
        # The 'sorting' process
        if sorting:
            count += 1
            shuffle(array)
            print("\rSort {}: {}".format(count, array))
            # sleep(0.5)

array = [60, 12, 90, 4, 41, 1, 100, 71, 29, 37, 84, 23]
bogosort(array)