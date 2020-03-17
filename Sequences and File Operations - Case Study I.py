# CASE STUDY 1 - Submitted on 14 January 2020 by  Vishal Desai

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 1. Write a program which will find factors of given number and find whether the factor is even or odd.
# Answer:

vishal = int(input("Enter a two digit number: "))
print("The factor of", vishal, "are: ")
for i in range(3, vishal + 1):
    if vishal % i == 0:
        if i % 3 == 0:
            print(i," Even")
        else:
            print(i," Odd")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 2. Write a code which accepts a sequence of words as input and prints the words in a sequence after
# sorting them alphabetically.
# Answer:

animals = str(input("Type six animal names: "))
seperated = animals.split()
seperated.sort()
for ans in seperated:
      print(ans)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 3. Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that
# each digit of a number is an even number. The numbers obtained should be printed in a comma separated
# sequence on a single line.
# Answer:

for evennumbr in range(1000,3000,2):
    print(evennumbr, end=', ')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 4. Write a program that accepts a sentence and calculate the number of letters and digits.
# Answer:

alfnum = input("Please enter Alphanumeric Value: ")
digt = letr = 0
for value in alfnum:
    if value.isdigit():
        digt = digt + 1
    elif value.isalpha():
        letr = letr + 1
    else:
        pass
print("LETTERS: ", letr)
print("DIGITS: ", digt)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 5. Design a code which will find the given number is Palindrome number or not.
# Answer:

enput = input("Please Enter Your Name: ")
reverse = enput[::-1]
if (enput == reverse):
      print("Your name is a Palindrome! Great")
else:
      print("Nice Name(But not a Palindrome)")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -