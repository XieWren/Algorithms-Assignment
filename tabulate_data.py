from tabulate import tabulate

def tabulate_data(data):

    for index, element in enumerate(data):
        element["No."] = index + 1
        # print(element)
    # print(data)

    print('')
    print(tabulate(data, tablefmt = 'simple', headers = "keys", floatfmt = ".2f", colalign = ('left', 'left', 'left', 'right', 'right')))
    print('')