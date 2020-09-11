#! usr/bin/env python3.7

import sys
import fileinput

# DNA_Count Python3.7 Script that takes a file from command line arguments 
# and counts the number of A, C, G, T's. Than Prints the output to Standard Out.

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the
# symbols 'A', 'C', 'G', and 'T' occur in s

# Written by Marcus W. on September 10, 2020

# Welcome to DNA count the nucleotides A, C, G, T Program in Python

#Initialize Variables
varA = 0
varC = 0
varG = 0
varT = 0

# Find and assign the text file to a variable through the command line using imported sys.
dna_File = sys.argv[1]
print("The file argument is " + dna_File)

# Open the text file
dnaSequence = open(dna_File)
# print("The sequence is: " + dnaSequence)

# The following is a testing line while the program is running.
print("The program is parsing.")

# Loop to parse the muilti-fasta file inside a loop to go through gene name text file, increasing each integer as it is spotted.
for lines in dnaSequence:
	for char in lines:
		if(char == 'A'):
			varA = varA + 1
			print(varA)
		elif(char == 'C'):
			varC = varC + 1
			print(varC)
		elif(char == 'G'):
			varG = varG + 1
			print(varG)
		elif(char == 'T'):
			varT = varT + 1
			print(varT)

# Print the Results
print("A = {0}. C = {1}. G = {2}. T = {3}".format(varA, varC, varG, varT))

# Close files to end program
dnaSequence.close()