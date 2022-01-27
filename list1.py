from timeit import Timer
import matplotlib.pyplot as plt


def check_time_max_value():
    global maximum_value

    first_list = [1,2,3,4,345,2234,2244,221155,234453,66432]
    maximum_value = max(first_list)

    return maximum_value


if __name__=='__main__':
    t = Timer("check_time_max_value()", "from __main__ import check_time_max_value")
    plt.show()
    print(f'The maximum value is: {check_time_max_value()}')
    print(f'The time complexity to find the maximum value in a list is: {t.timeit()}')




