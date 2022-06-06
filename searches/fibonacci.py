from sys import path as sys_path
from os import path as os_path

current = os_path.dirname(os_path.realpath(__file__))
parent = os_path.dirname(current)

sys_path.append(parent)

from tabulate_data import tabulate_data

def fibonacci_search(array, key, search, action = "Update", replacement = None):
    start = -1
    found = []

    # Using Fibonacci values as a range to focus on within the array.
    # Useful for systems where * and / are memory intensive.

    # Initialise Fibonacci indexes
    fibo_low = 0
    fibo_mid = 1
    fibo_high = fibo_mid + fibo_low
    
    # Get Fibonacci indexes to (1 iteration above) highest values to cover range
    # Ensure array parts are split as large as possible
    while fibo_high < len(array):
        
        # fibo_low used to calculate focusedIndex
        fibo_low = fibo_mid
        fibo_mid = fibo_high

        fibo_high = fibo_mid + fibo_low


    # Moving down each fibonacci_iteration, to approx. half the array.
    # fibo_high <= 1 means the range of possibilities has reached 0, and thus the search ends.
    while fibo_high > 1:

        #Note: Searching after the 'start' factor
        #To ensure index is within range, use max value of array if larger than array length
        if start + fibo_low > len(array) - 1:
            focusedIndex = len(array) - 1
        else:
            focusedIndex = start + fibo_low
        # focusedIndex = min(start + fibo_low, len(array) - 1)
        
        """
        print('\nFocusedIndex:', focusedIndex)
        print('Start:', start)
        print('Fibo_low:', fibo_low, '\tFibo_mid:', fibo_mid, '\tFibo_high:', fibo_high)
        """        

        record = array[focusedIndex]

        # Index found
        if record[key] == search:
            
            # Add to array of found values
            found.append(array.pop(focusedIndex))

            # Prevent index error
            while focusedIndex < len(array):

                # Check direct neighbour elements (-->)
                if array[focusedIndex][key] == search:
                    found.append(array.pop(focusedIndex))
                else:
                    break

            # Prevent array[-1]
            while focusedIndex > 0:

                # Check direct neighbour elements (<--)
                focusedIndex -= 1
                
                if array[focusedIndex][key] == search:
                    found.append(array.pop(focusedIndex))
                else:
                    break

            # Done with checking
            break


        #Element is in first 1/2 (approx.) of array still remaining
        elif record[key] > search:   

            # Move fibo_high down 2 Fibonacci iterations
            # Temporarily decrement
            fibo_high = fibo_low             # fibo_high: 13 -> 5
            fibo_mid = fibo_mid - fibo_low   # fibo_mid:   8 -> 3
            fibo_low = fibo_high - fibo_mid  # fibo_low:   5 -> 2


        #Element is in second 1/2 (approx.) of array still remaining
        else:
            
            # Move fibo_high down 1 Fibonacci iteration
            # Temporarily decrement
            fibo_high = fibo_mid             # fibo_high: 13 -> 8
            fibo_mid = fibo_low              # fibo_mid:   8 -> 5
            fibo_low = fibo_high - fibo_mid  # fibo_low:   5 -> 3

            # Push values forward to check off other values
            # Permanently increment
            start = focusedIndex

    if found == []:
        print("{}: {} cannot be found.".format(key, search))

    else:
        tabulate_data(found)
        
        if len(found) > 1:
            while True:
                try:
                    choice = int(input("Select item number: "))
                    if choice > len(found):
                        print("\033[91m" + "Error. Please enter a number from 1 to {}.".format(len(found)) + "\033[00m")
                        continue
                except:
                    print("\033[91m" + "Error. Please enter a number." + "\033[00m")
                    continue
                break
        else:
            # No need to ask for choice since only one item found
            print("Select item number: 1")
            choice = 1

        if action == "Update":
            # Confirm replacement
            check = input("Replace {}: {} with {}? (Y/N): ". format(key, search, replacement)).upper()
            while check != 'Y' and check != 'N':
                print("\033[91m" + "Please only enter 'Y' or 'N'." + "\033[00m")
                check = input("Replace {}: {} with {}? (Y/N): ". format(key, search, replacement)).upper()

            if check == "Y":
                # Replace value
                found[choice - 1][key] = replacement
                print("{}: {} has been replaced with {}.".format(key, search, replacement))

        elif action == "Delete":
            # Confirm deletion
            check = input("Delete {}: {}? (Y/N): ". format(key, search)).upper()
            while check != 'Y' and check != 'N':
                print("\033[91m" + "Please only enter 'Y' or 'N'." + "\033[00m")
                check = input("Delete {}: {}? (Y/N): ". format(key, search)).upper()

            if check == "Y":
                # Replace value
                print(choice)
                found.pop(choice - 1)
                print("{}: {} has been deleted.".format(key, search))
        
        array += found

# Testing
if __name__ == "__main__":

    from sorts.comb import comb_sort

    array = [
             {
              'No.': 1,
              'Package': 'Golden Gate', 
              'Customer': 'Vincent van Helsing', 
              'Pax': 3, 
              'Cost': 227
             },

             {
              'No.': 2,
              'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 
              'Customer': 'Eduard von Hartmann', 
              'Pax': 2, 
              'Cost': 238
             }, 

             {
              'No.': 3,
              'Package': 'Special Number 3.', 
              'Customer': 'James Tay', 
              'Pax': 4, 
              'Cost': 198
             }, 

             {
              'No.': 4,
              'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 
              'Customer': 'Alice Margatroid', 
              'Pax': 2, 
              'Cost': 150
             },

             {
              'No.': 5,
              'Package': 'Furry Friends', 
              'Customer': 'Vincent van Helsing', 
              'Pax': 3, 
              'Cost': 288
             }, 

             {
              'No.': 6,
              'Package': 'Australia.', 
              'Customer': 'Elon Musk', 
              'Pax': 5, 
              'Cost': 273
             },

             {
              'No.': 7,
              'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 
              'Customer': 'John Lim', 
              'Pax': 1, 
              'Cost': 164}, 

             {
              'No.': 8,
              'Package': 'Honeymoon Suite', 
              'Customer': 'Lancelot R. Gilligrass', 
              'Pax': 3, 
              'Cost': 393
             },

             {
              'No.': 9,
              'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 
              'Customer': 'Eduard von Hartmann', 
              'Pax': 5, 
              'Cost': 269
             }, 

             {
              'No.': 10,
              'Package': 'Fun with Family', 
              'Customer': 'Alice Margatroid', 
              'Pax': 5, 
              'Cost': 271
             }
            ]

    comb_sort(array, 'Customer')

    tabulate_data(array)
    fibonacci_search(array, 'Customer', 'Alice Margatroid', 'Delete')
    tabulate_data(array)