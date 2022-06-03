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

if __name__ == "__init__":
    from tabulate_data import tabulate_data