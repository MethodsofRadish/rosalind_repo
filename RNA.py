#! usr/bin/env python3.7

import sys
import fileinput

# DNA_Count Python3.7 Script that takes a file from command line arguments 
# and counts the number of A, C, G, T's. Than Prints the output to Standard Output.

# Written by Marcus W. on September 11, 2020

# Welcome to DNA to RNA Program in Python 3.7
# This program takes a .txt file of DNA nucleotides (A,T,C,G) and converts
# the DNA sequence to RNA (A,U,C,G) than prints the new sequence to a file.

# Get file from Command Line Argument.
dna_File = sys.argv[1]

# Open the muilti-fasta file
dnaSequence = open(dna_File)
# print("The sequence is: " + dnaSequence)

# Loop to parse the muilti-fasta file inside a loop to go through gene name text file
for lines in dnaSequence:
	for char in lines:
		if(char == 'A'):
			print('A', end = "")
		elif(char == 'C'):
			print('C', end = "")
		elif(char == 'G'):
			print('G', end = "")
		elif(char == 'T'):
			print('U', end = "")
print("", end = " ")

# Close files to end program
dnaSequence.close()