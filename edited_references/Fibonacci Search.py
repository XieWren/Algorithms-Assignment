def fibonacci_search(array,search):
    start = -1

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

        focusedElement = array[focusedIndex]

        # Index found
        if focusedElement == search:
            return focusedIndex

        #Element is in first 1/2 (approx.) of array still remaining
        elif focusedElement > search:   

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

    return -1

for n in range(10):
    print('\nResult:', fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9], n))

# print(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

"""
⬆: focusedIndex
X: Permanently passed over
O: Temporarily moved forward; can be decremented

Search: 4

Start: -1     Fibo_low: 5     FocusedIndex: 4

  [1, 2, 3, 4, 5, 6, 7, 8, 9]
X              ⬆                <-- Values incremented forward by start
X━━O━━O━━O━━O━━┛                <-- Fibonacci value manipulation

    ⬇         ⬇
    ⬇ Squeeze ⬇
    ⬇         ⬇

Start: -1     Fibo_low: 2     FocusedIndex: 1

  [1, 2, 3, 4, 5, 6, 7, 8, 9]
X     ⬆
X━━O━━┛

    ⬇         ⬇
    ⬇ Push ⮕ ⬇
    ⬇         ⬇

Start: 1      Fibo_low: 1     FocusedIndex: 2     

  [1, 2, 3, 4, 5, 6, 7, 8, 9]
   X     ⬆
   ┗━━O━━┛

    ⬇         ⬇
    ⬇ Push ⮕ ⬇
    ⬇         ⬇

Start: 2      Fibo_low: 1     FocusedIndex: 3

  [1, 2, 3, 4, 5, 6, 7, 8, 9]
   X━━X     ⬆
      ┗━━O━━┛

Result: 3


Search: 7

Start: -1    Fibo_low: 5     FocusedIndex: 4

  [1, 2, 3, 4, 5, 6, 7, 8, 9]
X              ⬆
X━━O━━O━━O━━O━━┛

    ⬇         ⬇
    ⬇ Push ⮕ ⬇
    ⬇         ⬇

Start: 4     Fibo_low: 3     FocusedIndex: 7

[1, 2, 3, 4, 5, 6, 7, 8, 9]
 X━━X━━X━━X           ⬆
          ┗━━O━━O━━O━━┛

    ⬇         ⬇
    ⬇ Squeeze ⬇
    ⬇         ⬇

Start: 4     Fibo_low: 1     FocusedIndex: 5

[1, 2, 3, 4, 5, 6, 7, 8, 9]
 X━━X━━X━━X     ⬆
          ┗━━O━━┛

    ⬇         ⬇
    ⬇ Push ⮕ ⬇
    ⬇         ⬇

Start: 5     Fibo_low: 1     FocusedIndex: 6

[1, 2, 3, 4, 5, 6, 7, 8, 9]
 X━━X━━X━━X━━X     ⬆
             ┗━━O━━┛

Result: 6
"""