# Mary McHale, 27th March 2018
# Exercise 6 based on Factorial numbers
# Asked to " Write a Python script that containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial."
# The factorial of a number is that number multiplied by all of the positive numbers less than it. 
# For example, the factorial of 5 is 5x4x3x2x1 which equals 120. You should, in your script, test the function by calling it with the values 5, 7, and 10.


n = input ("Please type a positive number between 1 and 20: ")
# Asking the user for inout
n=int(n)
# using the int function which lets you read integers as numbers
print (n)
m = n + 1
# m is the maximum number, integer plus 1 is higher than 21(20 + 1)

a = 1
# Counter for a. So for 5 its multiplied *1*2*3*4
c = 1
# counter for c..where c is increased by 1 each time..1,2,3,4,etc

while c < m:
    a = a * c
    c = c + 1

print(a, "is the answer.")

