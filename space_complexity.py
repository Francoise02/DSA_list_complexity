

from memory_profiler import profile
@profile

def my_func():
    a = [1] #* (10 ** 6)
    b = [2] #* (2 * 10 ** 7)
    del b
    #print
    return a

if __name__ == '__main__':
    my_func()

#-m memory_profiler example.py-m memory_profiler example.py