# Write report
# Patience, bead (gravity), bitonic, piegeonhole, shell, radix

from random import randint, choice

from searches.linear import *
from searches.binary import *
from searches.fibonacci import *
from searches.range import *

from sorts.bubble import *
from sorts.selection import *
from sorts.insertion import *
from sorts.cocktail import *
from sorts.heap import *
from sorts.tree import *
from sorts.gnome import *
from sorts.comb import *
from sorts.bogo import *

from tabulate_data import tabulate_data

def get_direction():
    while True:
        try:
            direction = int(input("\n1. Ascending\n2. Descending\n\nSort Direction:\n"))
            if direction != 1 and direction != 2:
                print("\033[1;91m" + "Error. Please enter '1' or '2'." + "\033[00m")
                continue
            break
        except:
            print("\033[1;91m" + "Error. PLease enter a number." + "\033[00m")
            continue
    if direction == 1:
        return "A"
    else:
        return "D"

packages = ['Student Saver', 'Fun with Family', 'Ultimate Deluxe', 'Honeymoon Suite', 'Australia.', 'Furry Friends', 'Breakfast Menu', 'Lunch Menu', 'Dinner Menu', 'Pool View', 'Golden Gate', 'Special Number 3.', 'Winter Moon', 'Summer Days', 'Birthday Banquet', 'Classic', 'Lucky Package']
customers = ['Elon Musk', 'Alice Margatroid', 'Lancelot R. Gilligrass', 'Gordon Freeman', 'Ronald McDonald', 'Vincent van Helsing', 'Luna Lovegood', 'Eduard von Hartmann', 'Cherry', 'Moss', 'James Tay', 'John Lim', 'Gilbert Chan', 'Lucky Customer']

data = []

for count in range(1, 11):
    data.append({'No.': count,
                 'Customer': choice(customers),
                 'Package': choice(packages),
                 'Pax': randint(1, 5),
                 'Cost': randint(900, 4500)/10})

choice = 0
while choice != 'q':
    choice = input("""
Please make your selection:
1: Display all records
2: Sort record by Customer Name using Bubble sort 
3: Sort record by Package Name using Selection sort 
4: Sort record by Package Cost using Insertion sort
5: Search record by Customer Name using Linear Search and update record 
6: Search record by Package Name using Binary Search and update record
7: List records range from $X to $Y (e:g $100-$200)
8: Custom Selection (ft. more options)

9: Add Record

Q: Exit Application
""")
    if choice == '1':
        count = 1
        if data != []:
            tabulate_data(data)

        else:
            print("No customer information in database.")

    elif choice == '2':
        bubble_sort(data, 'Customer', get_direction())

    elif choice == '3':
        selection_sort(data, 'Package', get_direction())

    elif choice == '4':
        insertion_sort(data, 'Cost', get_direction())

    elif choice == '5':
        old = input("Old customer name: ")
        new = input("New customer name: ")

        linear_search(data, 'Customer', old, replacement = new)

    elif choice == '6':
        old = input("Old package name: ")
        new = input("New package name: ")

        insertion_sort(data, 'Package')

        binary_search(data, 'Package', old, replacement = new)

    elif choice == '7':

        while True:

            try:
                lower = float(input("Lower range: "))
                upper = float(input("Upper range: "))
                
                if lower > upper:
                    # Red Text
                    print("\033[1;91m" + "Error. Lower range must be lesser than upper range.\n" + "\033[00m")
                    
                    continue

            except:
                # Red Text
                print("\033[1;91m" + "Error. Please enter a number.\n" + "\033[00m")

                continue

            break
        
        # Sort ascending
        insertion_sort(data, "Cost")

        search_range(data, lower, upper)

    elif choice == '8':

        while True:
            advanced = input("""
Searches:
‾‾‾‾‾‾‾‾‾
1:  Linear
2:  Binary
3:  Fibonacci*

Sorts:
‾‾‾‾‾‾
4:  Bubble
5:  Selection
6:  Insertion
7:  Cocktail-Shaker*
8:  Heap*
9:  Tree*
10: Gnome*
11: Comb*
12: Bogo*

Q:  Quit

Please make your selection:
""").upper()

            searches = ['Customer', 'Package', 'Pax', 'Cost']

            if advanced == 'Q':
                break

            elif advanced in ['1', '2', '3']:

                while True:
                    try:
                        action = int(input("\n1. Update Record\n2. Delete Record\n\nAction:\n"))
                        if action != 1 and action != 2:
                            print("\033[1;91m" + "Error. Please enter '1' or '2'." + "\033[00m")
                            continue
                        break
                    except:
                        print("\033[1;91m" + "Error. Please enter a number." + "\033[00m")
                        continue
                if action == 1:
                    action = "Update"
                else:
                    action = "Delete"



                while True:
                    try:
                        searching = int(input("\n1. Customer Name\n2. Package Name\n3. Number of Pax\n4. Package Cost\n\nSearch For:\n"))
                        if searching > 4 or searching < 1:
                            print("\033[1;91m" + "Error, please try again." + "\033[00m")
                            continue
                        break
                    except:
                        print("\033[1;91m" + "Error, please try again." + "\033[00m")
                        continue


                if action == "Update":
                    while True:
                        search = input("Old value: ")
                        replacement = input("New value: ")
                        if searching == 3:
                            try:
                                if int(search) - float(search) != 0.0 and int(replacement) - float(replacement) != 0.0:
                                    print("\033[1;91m" + "Error, please try again." + "\033[00m")
                                    continue
                            except:
                                print("\033[1;91m" + "Error, please try again." + "\033[00m")
                                continue
                            search = int(search)
                            replacement = int(replacement)
                        break
                elif action == "Delete":
                    search = input("Values to delete: ")
                    replacement = None


                key = searches[searching - 1]

                insertion_sort(data, key)

                if advanced == '1':
                    linear_search(data, key, search, action, replacement)
                elif advanced == '2':
                    binary_search(data, key, search, action, replacement)
                else:
                    fibonacci_search(data, key, search, action, replacement)


            elif advanced in ['4', '5', '6', '7', '8', '9', '10', '11', '12']:

                while True:
                    try:
                        searching = int(input("\n1. Package Name\n2. Customer Name\n3. Number of Pax\n4. Package Cost\n\nSort Based On:\n"))
                        if searching > 4 or searching < 1:
                            print("\033[1;91m" + "Error, please try again." + "\033[00m")
                            continue
                        break
                    except:
                        print("\033[1;91m" + "Error, please try again." + "\033[00m")
                        continue

                key = searches[searching - 1]
                direction = get_direction()

                if advanced == '4':
                    bubble_sort(data, key, direction)
                elif advanced == '5':
                    selection_sort(data, key, direction)
                elif advanced == '6':
                    insertion_sort(data, key, direction)
                elif advanced == '7':
                    cocktail_shaker_sort(data, key, direction)
                elif advanced == '8':
                    heap_sort(data, key, direction)
                elif advanced == '9':
                    tree_sort(data, key, direction)
                elif advanced == '10':
                    gnome_sort(data, key, direction)
                elif advanced == "11":
                    comb_sort(data, key, direction)
                elif advanced == "12":
                    check = input("\033\n[1;91m" + "Are you sure you would like to run Bogosort? (Y/N)\n" + "\033[00m").upper()
                    while check != "Y" and check != "N":
                        check = input("\033[1;91m" + "Are you sure you would like to run Bogosort? (Y/N)\n" + "\033[00m").upper()
                    if check == "Y":
                        bogo_sort(data, key, direction)



            else:
                # Red Text
                print("\033[1;91m" + "Error, please try again." + "\033[00m")

    elif choice == '9':


        package = input("Enter Package Name: ")
        while package.isspace() or package == "":
            print("\033[1;91m" + "Input must contain readable text. Try again." + "\033[00m")
            package = input("Enter Package Name: ")


        customer = input("Enter Customer Name: ")
        while customer.isspace() or customer == "":
            print("\033[1;91m" + "Input must contain readable text. Try again." + "\033[00m")
            customer = input("Enter Customer Name: ")


        while True:
            try:
                pax = float(input("Enter number of pax: "))
                if pax < 0:
                    print("\033[1;91m" + "Cost must not be negative. Try again." + "\033[00m")
                    continue
                if pax - int(pax) != 0.0:
                    print("\033[1;91m" + "Cost must be a whole number." + "\033[00m")
                    continue
            except:
                print("\033[1;91m" + "Cost must be a number. Try again." + "\033[00m")
                continue
            pax = int(pax)
            break

        

        while True:
            try:
                cost = float(input("Enter Package Cost ($): "))
                if cost < 0:
                    print("\033[1;91m" + "Cost must not be negative. Try again." + "\033[00m")
                    continue
            except:
                print("\033[1;91m" + "Cost must be a number. Try again." + "\033[00m")
                continue
            cost = round(cost, 2)
            break


        data.append({
                     'No.': len(data) + 1,
                     'Package': package,
                     'Customer': customer,
                     'Pax': pax,
                     'Cost': cost
                     })

    elif choice.upper() == 'Q':
        print("Thank you for using this service.")
        break

    else:
        # Red Text
        print("\033[1;91m" + "Error, please try again." + "\033[00m")
