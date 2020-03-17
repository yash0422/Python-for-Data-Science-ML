# CASE STUDY 1 - Submitted on 15 January 2020 by  Vishal Desai

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 1. What is the output of the following code?
# Answer: 4
nums = set([1,1,2,3,3,3,4,4]);
print(len(nums))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 2. What will be the output?
# Answer: 'john' and 'peter'
d = {"john": 40, "peter": 45}
print(list(d.keys()))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 3. A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password:
# 1. At least 1 small case letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 capital letter between [A-Z]
# 4. At least 1 special character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
# Answer:
import re
password = input("Please Enter Password: ")
Flag = True
while Flag:
    if (len(password) < 6 or len(password) > 12):
        break
    elif not re.search("[a-z]", password):
       break
    elif not re.search("[0-9]", password):
        break
    elif not re.search("[A-Z]", password):
        break
    elif not re.search("[$#@]", password):
        break
    elif re.search("\s", password):
        break
    else:
        print("Valid Password")
        Flag = False
        break
if Flag:
    print("Password must contain atleast 1 character from - \n"
          "[a-z]  [A-Z]  [0-9]  [$#@]")

'''
# Failed Attempt
password = input("Please Enter Password: ")
digt = smlletr = splchr =  capletr = 0
for value in password:
    if value.isdigit():
        digt = digt + 1
    elif value.islower():
        smlletr = smlletr + 1
    elif value.isupper():
        capletr = capletr + 1
    elif value.isascii():
        splchr = splchr + 1
    elif len(value) < 6:
        print("Mimimum 6 Character needed")
    elif len(value) > 12:
        print("Maximum 12 allowed.")
    elif value.isdigit() != False:
        print("Please use 1 number")
    else:
        pass
print(digt)
print(smlletr)
print(splchr)
print(capletr)
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 4. Write a for loop that prints all elements of a list and their position in the list.
# Answer:
a = [4,7,3,2,5,]
for i, val in enumerate(a):
    print(i, ',', val)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 5. Please write a program which accepts a string from console and print the characters
# that have even indexes.
# Answer:
userinput = input("Enter a String:")
if userinput:
    string = ""
    for i in userinput:
        if userinput.index(i) % 2 == 0:
            string += str(i)
    print(string)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 6. Please write a program which accepts a string from console and print it in reverse order.
# Answer:
def temp(string):
    string = string[::-1]
    return string
userinput = input("Please Enter Input: ")
print(temp(userinput), end="")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 7. Please write a program which count and print the numbers of each character in a string input by console.
# Answer:
userinput = input("Please Enter Input: ")
for letter in range(ord('a'),ord('z')+1):
    letter = chr(letter)
    cont = userinput.count(letter)
    if cont > 0:
        print("{},{}".format(letter, cont))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 8.With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list
# whose elements are intersection of the above given lists.
# Answer:
listone = {1, 3, 6, 78, 35, 55}
listtwo = {12, 24, 35, 24, 88, 120, 155}
listone &= listtwo
listtwo = list(listone)
print(listtwo)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 9.By using list comprehension, please write a program to print the list after removing the
# value 24 in [12,24,35,24,88,120,155].
# Answer:
givenlist = [12, 24, 35, 70, 88, 120, 155]
givenlist = [x for x in givenlist if x!=24]
print(givenlist)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 10. By using list comprehension, please write a program to print the list after removing the
# 0th,4th,5th numbers in [12,24,35,70,88,120,155]
# Answer:
gvnlst = [12, 24, 35, 70, 88, 120, 155]
gvnlst = [x for (i,x) in enumerate(gvnlst) if i not in (0,4,5)]
print(gvnlst)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 11.By using list comprehension, please write a program to print the list after removing delete
# numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
# Answer:
gvnnlist = [12,24,35,70,88,120,155]
gvnnlist = [x for x in gvnnlist if x%5!= 0 and x%7!= 0]
print(gvnnlist)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 12.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0)
# !!!
# Sorry couldn't understand and solve the question, will get explain by instructor in coming lectures

