from timeit import Timer

def check_time_strings():
    global mystring
    global lower_string

    mystring = input('Enter any string: ')
    lower_string = mystring.lower()

    return lower_string


if __name__=='__main__':
    t = Timer("check_time_strings()", "from __main__ import check_time_strings")
    print(f'The lower form of your input is: {check_time_strings()}')
    print(f'The time complexity to find the maximum value in a list is: {t.timeit()}')


