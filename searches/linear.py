def linear_search(array, key, search, action = "Update", replacement = None):

    found = []
    focusedIndex = 0
    
    while focusedIndex < len(array):

        record = array[focusedIndex]

        if record[key] == search:

            # Add to array of found values
            found.append(array.pop(focusedIndex))

        focusedIndex += 1

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

    from sys import path as sys_path
    from os import path as os_path

    current = os_path.dirname(os_path.realpath(__file__))
    parent = os_path.dirname(current)

    sys_path.append(parent)

    from tabulate_data import tabulate_data
    

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

    tabulate_data(array)
    linear_search(array, 'Customer', 'Alice Margatroid', 'Delete')
    tabulate_data(array)

    