# 002 Deep Dive – Functions, OOPs, Modules, Errors and Exceptions
# Case Study I

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 1. A Robot moves in a Plane starting from the origin point (0,0).
# The robot can move toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:
# UP 5DOWN 3LEFT 3RIGHT 2The numbers after directions are steps.
# Write a program to compute the distance current position after sequence of movements.

# Answer: Sorry was not able to solve, as didn't understand the question and what logic to apply.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 2.Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
# Answer


def BinarySearch(data_of_xyz, search_key):
    low_indx = 0
    hig_indx = len(data_of_xyz) -1
    found = False
    while low_indx<=hig_indx and not found:
        mid_indx = (low_indx + hig_indx) // 2
        if search_key == data_of_xyz[mid_indx]:
            found = True
        elif search_key > data_of_xyz[mid_indx]:
            low_indx = mid_indx + 1
        else:
            hig_indx = mid_indx - 1
    if found:
        print("Your search key is at position: ", mid_indx)
    else:
        print("Your key is not found: ")

data_of_xyz = [13, 24, 32, 35, 78]
data_of_xyz.sort()
print(data_of_xyz)
search_key = int(input("Enter the required key: "))
BinarySearch(data_of_xyz,search_key)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 3.Weather forecasting organization wants to show is it day or night. So, write a program for such organization
# to findwhether is it dark outside or not.
# Answer

import time
lcltime = time.localtime()
if lcltime.tm_hour < 12:
    print("Hey! Wakeup it's a Good Morning!")
else:
    print("Time to Relax!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 4. Write a program to find distance between two locations when their latitude and longitudes are given.
# Answer

from math import radians, cos, sin, asin, sqrt
def distance(latitude_1, latitude_2, longitude_1, longitude_2):

    latitude_1 = radians(latitude_1)
    latitude_2 = radians(latitude_2)
    longitude_1 = radians(longitude_1)
    longitude_2 = radians(longitude_2)

    dis_longi = longitude_2 - longitude_1
    dis_lati = latitude_2 - latitude_1
    a = sin(dis_lati / 2) ** 2 + cos(latitude_1) * cos(latitude_2) * sin(dis_longi / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return(c * r)

latitude_1 = 23.4241
latitude_2 = 19.0760
longitude_1 = 53.8478
longitude_2 = 72.8777
print(distance(latitude_1, latitude_2, longitude_1, longitude_2), "KM")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 5.Design a software for bank system. There should be options like cash withdraw, cash credit and change password.
# According to user input, the software should provide required output.
# Answer:

# define function to check the pin code
def enterpin():
    pin = int(input("\nPlease Enter your 4 digit PIN\nHere >>"))
    if pin == 1234:
        print("Valid Pin")
    else:
        print("Invalid Pin! Please try again")

# define function for cash withdrawal
def withdrawal():
    amount = int(input("\nPlease Enter the amount: "))
    if amount > 5000:
        print("You don't have enough balance for this amount of withdrawal")
        return withdrawal()
    else:
        print("\nYour entered amount is:", amount,"\nYour new balance after withdrawal is", 5000 - amount)
        return operation()

# define function for cash deposit
def cashdeposit():
    currentbalance = 5000
    amount = int(input("\nPlease Enter the amount you wish to deposit: "))
    if amount < 0:
        print("Your entered amount is:", amount,"\nYour new balance after deposit is", 5000 + amount)
    else:
        print("Your entered amount is:", amount,"\nYour new balance after deposit is", 5000 + amount)
        return operation()

# define function to change pin
def changepin():
    currentpin = 1234
    newpin = int(input("Please enter your old PIN No.: "))
    if newpin == currentpin:
        print(int(input("Please enter your new PIN: ")))
    if newpin != currentpin:
        print("You entered a wrong current Pin!")
        return changepin()
    else:
        print("Is you new Pin!")
        print( )
        print(operation())

# define function to exit programme
def exit():
    print("*** Thank for banking with us! ***")

# define parent function or operation
def operation():
    print("\nWelcome to XYZ Bank\n\nPlease choose your desired transaction from list below:\n\n"
          "1. Cash Withdrawal. 2. Cash Deposit. 3. Change PIN. 4. Exit")
    selection = int(input("Please Enter: "))
    if selection == 1:
        print( )
        print(enterpin())
        print(withdrawal())
    if selection == 2:
        print(enterpin())
        print(cashdeposit())
    if selection == 3:
        print(enterpin())
        print(changepin())
    if selection == 4:
        print(exit())

# call command
operation()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 6.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included). The numbers obtained should be printed in
# a comma-separated sequence on a single line.

mptyset = []
for x in range(2000, 3200):
    if (x % 7) == 0:
        y = x / 5.0
        if (y % 5) != 0:
            emptyset.append(str(x))
print(", ".join(emptyset))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 7. Write a program which can compute the factorial of a given numbers. Use recursion to find it.
# Answer
def rucr_factrl(n):
    '''this function finds factorial of
    given nummber'''
    if n == 1:
        # factorial of 1 is 1 so we need to return
        return n
    else:
        return n * rucr_factrl(n - 1)

# collect input from user
usrinput = int(input("Enter positive number,\n"
                     "as negative numbers factorial in Nan\n"
                     "and factorial of 0 is 1\n"
                     "Your desired input: "))

print("The factorial of your input number", usrinput, "is", rucr_factrl(usrinput))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 8.Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Answer:

import math
C = 50
H = 30
emtlst = []
result =[]
usrinput=input("Please enter 100,150,180: ")
emtlst=usrinput.split(",")
emtlst = [int(i) for i in emtlst]
i=0
l = len(emtlst)
while(i<l):
    Q = round(math.sqrt((2 * C * emtlst[i]) / H))
    result.append(Q)
    i+=1
print("output=",result)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 9.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.Note: i=0,1.., X-1; j=0,1,¡-Y-1.

numofrows = int(input("Desired number of Rows: "))
numofcolm = int(input("Desired number of Columns: "))

multi_list = [[0 for col in range(numofcolm)] for row in range(numofrows)]

for row in range(numofrows):
    for col in range(numofcolm):
        multi_list[row][col] = row*col

print(multi_list)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 10. Write a program that accepts a comma separated sequence of words as input and prints the words
# in a comma-separated sequence after sorting them alphabetically.

usr_input = input("Enter few name so animal: ").split(",")
lst = list(usr_input)
lstone = len(lst)

srtedlist = sorted(lst)
lst = srtedlist

for i in range (lstone):
    if i == lstone-1:
        print(lst[i],end="")
    else:
        print(lst[i],end=",")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 11. Write a program that accepts sequence of lines as input and prints the lines after making
# all characters in the sentence capitalized.
# Answer:

inp1 = input("Please enter text: ")
inp2 = input("> ")
#print(name.capitalize().upper())
print(inp1.upper())
print(inp2.upper())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 12. Write a program that accepts a sequence of whitespace separated words as input and prints the words
# after removing all duplicate words and sorting them alphanumerically.
# Answer:

inp1 = "zebra, tiger, lion, fox, alligator"
splt = inp1.split(" ")
splt.sort()

print("Sorted Alphabetically: ")

for word in splt:
    print((word).capitalize(), end=" ",)
    #print(word, end=" ",)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 13. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be
# printed in a comma separated sequence
# Answer

hanger = []
its = [lookup for lookup in input("Enter: ").split(',')]
for p in its:
    intp = int(p, 2)
    if not intp%5:
        hanger.append(p)

print(','.join(hanger))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 14. Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case
# letters and lower case letters.
# Answer:

usrinpt = input("Enter string: ")
lowcs=0
uppcs=0

for answer in usrinpt:
      if (answer.islower()):
            lowcs = lowcs + 1
      elif (answer.isupper()):
            uppcs = uppcs + 1
      elif (answer.isnumeric() and answer.isalnum() and answer.isascii()):
          print("Please enter words only: ")


print("Lowercase Characters are: ", lowcs,
      "\nUppercase Characters are: ", uppcs)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

