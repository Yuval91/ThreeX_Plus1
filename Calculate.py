import numpy as np

def check(num_str):
    # works only for small numbers
    a = int(num_str)
    # while a != 1:
    for i in range(10):
        if a%2:
            a = 3*a
            a += 1
        else:
            a = int(a/2)
        print(a)


def convert_to_array(st):
    num = []
    for s in st:
        num.append(int(s))
    # the ones are at place 0, tens in place 1 etc.
    return num[::-1]
    
    
def threeX_plus1(arr):
    new = []
    tmp = 0
    # starts at the low digits - iterate "normaly"
    for i in range(len(arr)):
        mul = arr[i]*3 + tmp
        new.append(mul%10)
        tmp = int(mul/10)
        # print(f"new = {new}, mul = {mul}, tmp = {tmp}")
    if tmp > 0:
        new.append(tmp)
    
    # add one and propogate
    for i in range(len(new)):
        if new[i] == 9:
            new[i] = 0
        else:
            new[i] += 1
            break
    
    return new


def devide_by_two(arr):
    new = []
    tmp = 0
    # starts at the high digit - iterate from end to start
    for i in range(len(arr), 0, -1):
        dev = arr[i-1] / 2.
        new.append(int(int(dev) + tmp))
        tmp = int((dev*10)%10)
    if new[0] == 0:
        new.pop(0)
    return new[::-1]

    
def print_num(arr):
    for i in range(len(arr), 0, -1):
        print(arr[i-1], end='')
    print("\n", end='')


def calculate(a, to_print = True):
    num_str = a
    arr = convert_to_array(num_str)
    count = 0
    while not (len(arr) == 1 and arr[0] == 1):
        if to_print:
            print_num(arr)
        if arr[0]%2:
            arr = threeX_plus1(arr)            
        else:
            arr = devide_by_two(arr)
        count += 1
    if to_print:
        print_num(arr)
    
    print(f"It took {count} steps to get to 1")

str_num = f"{np.random.randint(1, 10)}"
for i in range(1000):
    str_num = f"{str_num}{np.random.randint(10)}"

print(f"the number is {str_num}")
calculate(str_num, False)

