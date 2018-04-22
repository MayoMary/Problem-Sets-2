# Mary McHale, 24h March 2018
# https://projecteuler.net/problem=5
# Exercise 4 based on Project Euler Problem 5
# Asked to " Write a Python program using for and range to calculate the smallest positive number that is evenly divisible by all of the numbers from 1 to 20


print("program started")
# This lets the user know that the script is working. The calculation is not instant. It takes some minutes

good = 0
# This is the counter for the Outer loop 
limit = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20 
limit = limit + 1
# limit is the maximum number that the answer can be

for a in range(1, limit, 1):
    # print(a,"outerloop")
    
    good = 0
    for b in range(1, 21, 1):
                # print(b, "inner loop")
                if a % b ==0:
                    good = good + 1
    # print(good, "is value of good")
    if good == 20:
        print ((a),"is the answer")
        quit()

print("program ended")
