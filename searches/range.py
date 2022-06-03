def search_range(data, lower, upper):

    found = []

    for element in data:

        if lower <= element['Cost'] <= upper:
            found.append(element)
        elif element['Cost'] > upper:
            break

    if found == []:
        print("No record within price range.")
    else:
        tabulate_data(found)

if __name__ == "__main__":

    from sys import path as sys_path
    from os import path as os_path

    current = os_path.dirname(os_path.realpath(__file__))
    parent = os_path.dirname(current)

    sys_path.append(parent)

    from tabulate_data import tabulate_data
    from sorts.tree import tree_sort

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
    tree_sort(array, 'Cost')
    search_range(array, 100, 200)
    