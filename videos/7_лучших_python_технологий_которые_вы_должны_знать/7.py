from itertools import product


list_1 = [1, 2]
list_2 = [5, 6]
list_3 = [0, 5]


def lowqual_implementation():
    for a in list_1:
        for b in list_2:
            for c in list_3:
                print(a, b, c)


def implementation_of_normal_boys():
    for a, b, c in product(list_1, list_2, list_3):
        print(a, b, c)


lowqual_implementation()
print('\n\n')
implementation_of_normal_boys()