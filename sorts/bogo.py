def bogo_sort(array, key, direction = 'A'):

    from random import shuffle

    sorting = True
    count = 0

    while sorting:

        try:
            sorting = False
            
            # Check if sorted
            if len(array) > 1:
                # Compare each element to the next
                for index in range(len(array) - 1):

                    # Plan to 'sort' if unsorted
                    if (direction == "A" and array[index][key] > array[index + 1][key]) or (direction == "D" and array[index][key] < array[index + 1][key]):
                        sorting = True
                        break

            
            
            # The 'sorting' process
            if sorting:
                count += 1
                shuffle(array)
                # print("\rSort {}: {}".format(count, [value[key] for value in array]), end = "")
                # sleep(0.5)
        except KeyboardInterrupt:
            print("\nProcess Interrupted.")
            break

# Testing
if __name__ == "__main__":
    array = [
             {'Package': 'Golden Gate', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 227}, 
             {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 2, 'Cost': 238}, 
             {'Package': 'Special Number 3.', 'Customer': 'James Tay', 'Pax': 4, 'Cost': 198}, 
             {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Alice Margatroid', 'Pax': 2, 'Cost': 150}, 
             {'Package': 'Furry Friends', 'Customer': 'Vincent van Helsing', 'Pax': 3, 'Cost': 288}, 
             {'Package': 'Australia.', 'Customer': 'Elon Musk', 'Pax': 5, 'Cost': 273}
            ]
    # {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'John Lim', 'Pax': 1, 'Cost': 164}, {'Package': 'Honeymoon Suite', 'Customer': 'Lancelot R. Gilligrass', 'Pax': 3, 'Cost': 393}, {'Package': 'LUCKY [Selected]!! WHAT A [Big Shot]!!!', 'Customer': 'Eduard von Hartmann', 'Pax': 5, 'Cost': 269}, {'Package': 'Fun with Family', 'Customer': 'Alice Margatroid', 'Pax': 5, 'Cost': 271}
    
    bogo_sort(array, 'Pax', 'D')
    print("")
    for n in array:
        print(n['Pax'])