from icecream import ic

def strange_number_processing(a, b, c):
    if a > 0:
        ic()
        if b % 2 == 0:
            ic()
            return 93
        else:
            ic()
            if c < 3 or a == 2:
                ic()
                return 33
    else:
        ic()
        if b == 2:
            ic()
            if c > 3 or a > 9:
                ic()
                return 44
        else:
            ic()
            return 21

strange_number_processing(2, 3, 2)
