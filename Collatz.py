# Mary McHale, 4th March 2018
# Topic 3 Collatz exercise
# https://en.wikipedia.org/wiki/Collatz_conjecture
# int function is how to read integers as numbers
# Source of int function was https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-integers
# n != 1....reads as 'n does not equal 1' 

n = input ("Please type a positive number between 1 and 100: ")
# Asking the user for input
n=int(n)
# int function is how to read integers as numbers
print (n)

while n != 1:
  if n % 2 ==0:
    p = n/2
    print (p)
  if n % 2 !=0:
    p = (n * 3 ) + 1
    print (p)
  n = p


