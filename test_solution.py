
# Q.A (Question A)
import re

with open(r"c:\Users\personal\PycharmProjects\Bincom_assignment\python_class_test.html", 'r') as file:
    x=file.readlines()

# print (x)
colours = []

for colour in x:
    C_V = re.findall(r'<td>(.*)</td>', colour)
    if C_V:
        colours.append(C_V)

# print (colours)

colour_values =(colours[1::2])
print (colour_values)


# Q.B (Question B)

mon = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN".split(", ")
tues = "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE".split(", ")
wed = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE".split(", ")
thurs = "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN".split(", ")
fri = "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE".split(", ")

# print (mon)
dictionary1 ={i:mon.count(i) for i in mon}
dictionary2 ={i:tues.count(i) for i in tues}
dictionary3 ={i:wed.count(i) for i in wed}
dictionary4 ={i:thurs.count(i) for i in thurs}
dictionary5 ={i:fri.count(i) for i in fri}
print (dictionary1, '\n', dictionary2, '\n', dictionary3, '\n', dictionary4, '\n', dictionary5)

# Q.B1-4 (using pandas for statistics)
import pandas as pd
#

my_dict = {'GREEN': 10, 'YELLOW': 5, 'BROWN': 6, 'BLUE': 30, 'PINK': 5, 'ORANGE': 9, 'CREAM': 2, 'RED': 9, 'WHITE': 16, 'ARSH':1, 'BLEW':1, 'BLACK':1,}
df = pd.DataFrame(list(my_dict.items()),columns=['colour', 'frequency'])
print (df)

# mean using pandas
print("\n----------- Calculate Mean -----------\n")
print(df.mean())

#median using pandas
print("\n----------- Calculate Median -----------\n")
print(df.median())

#mode using pandas
print("\n----------- Calculate Mode -----------\n")
print(df.mode())

from collections import Counter  ## importing counter

new_colors = list(mon+tues+wed+thurs+fri)
colors_freq = dict(Counter(sorted(new_colors)))

 # mean
temp = list(set(mon+tues+wed+thurs+fri))
print("\n----------- Calculate Mean -----------\n")
print(f"The mean colour of shirt is {temp[int((len(temp)-1)/2)]}")

# mode colour
for i in colors_freq.keys():
    if colors_freq.get(i) == max(colors_freq.values()):
        print("\n----------- Calculate Mode -----------\n")
        print(f"The most worn colour throughout the week is {i}")


# median colour
from operator import itemgetter
sorted_colors_freq = dict(sorted(colors_freq.items(), key = itemgetter(1)))
sorted_colors_freq_list = list(sorted_colors_freq.keys())

print("\n----------- Calculate Median -----------\n")
print(f"The median colour of shirt is {sorted_colors_freq_list[int((len(sorted_colors_freq_list)-1)/2)]}")

# variance
print (df.var())
#


## A recursive algorithm to search for a number entered by a user
# Q.7

def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = int(input("Enter a number :"))

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


## Q. 8
## coversion of binary to decimal

import random
from random import sample
from string import digits


binary_num = "".join(sample(bin(int(digits)), 4))
print(int(binary_num, 2))


##

#fibonacci series
# Q.9

def calculateSum(n):
	if (n<=0):
		return 0

	fibo =[0]*(n+1)
	fibo[1]=1

	sm = fibo[0]+fibo[1]

	for i in range(2,n+1):
		fibo[i]=fibo[i-1]+fibo[i-2]
		sm+=fibo[i]

	return sm

n=50
print ("Sum of Fibonacci numbers is : ",calculateSum(n))


