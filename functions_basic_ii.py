
# Countdown 
from typing import NewType


def countdown(num):
    new=[]
    for x in range(num,-1,-1):
        new.append(x)
    return new
print(countdown(13))

# Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]
y=print_and_return([1,2])
print(y)

# First Plus Length 
def first_plus_length(list):
    x = list[0]
    y = len(list)
    return x + y
print(first_plus_length([1,2,3,4,5]))

# Values Greater than Second 
def values_greater_than_second(list):
    new_list = []
    if len(list) < 2:
        return ("false")
    else:
        for x in range(0,len(list),1):
            if list[x]> list[1]:
                new_list.append(list[x])
        print(len(new_list))
        return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# This Length, That Value
def this_length_that_value(size,value):
    list = []
    for x in range(0,size,1):
        list.append(value)
    return list
print(this_length_that_value(4,7))