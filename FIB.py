import sys

import fileinput

# Opoen the file and read in the data. 
file = open('rosalind_fib3.txt', 'r')
line = file.readline()

# Split the data into two variables, using default whitespace as the delimiter.
n, k = line.split()

# Function to calculate the number of rabbit pairs at the end of the nth month.
def fiboRabbits(n, k):
    # Create a list to store the number of rabbit pairs at each month.
    rabbits = [0, 1]

    # Loop through the months and calculate the number of rabbit pairs.
    month = 1
    for month in range(1, n):
        # Calculate the number of rabbit pairs at the end of the month.
        rabbits.append(rabbits[month] + k * rabbits[month - 1])
    
    # Print the number of rabbit pairs at the end of the nth month.
    print(rabbits[n])
    
    return

# Convert each variable into an integer to perform calculations. 
# n = # of months, k = # of rabbit offspring.
n = int(n)
k = int(k)

rabbitsTotal = 0

# Check to see if the input is valid.
if n <= 40 and k <= 5:
    rabbitsTotal = fiboRabbits(n, k)   
else:
    print("Data in file is not valid.")

