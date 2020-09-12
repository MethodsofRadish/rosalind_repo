#! usr/bin/env python3.7

import sys
import fileinput

# DNA_Count Python3.7 Script that takes a file from command line arguments 
# Prints the output to Standard Out.

# Written by Marcus W. on September 12, 2020

# Welcome to DNA to RNA Program in Python 3.7
# This program takes a .txt file of DNA nucleotides (A,T,C,G) and converts
# the DNA sequence to the complimentary DNA sequence. (A,T,C,G).
# Remember A=T and G---C  (5' ----- 3')
#                         (3' ----- 5')

# Assign file name from command line.
dna_File = sys.argv[1]
print("The file argument is " + dna_File)

# Open the muilti-fasta file. An extra step.
dnaSequence = open(dna_File)

# Loop to parse the muilti-fasta file inside a loop to go through gene name text file
lines = dnaSequence.readlines()

#Initialize Variables
seqList = []

for lined in lines:
	for char in lined:
		if(char == 'A'):
			print('T', end = "")
			seqList.append(char)
		elif(char == 'C'):
			print('G', end = "")
			seqList.append(char)
		elif(char == 'G'):
			print('C', end = "")
			seqList.append(char)
		elif(char == 'T'):
			print('A', end = "")
			seqList.append(char)
	print("")

# Reverse the string.
newseqList = seqList[::-1]

# Print the Lists to see what you have.
print(seqList)
print(newseqList)

# Convert the reversed string and print to standard out.
for i in newseqList:
	if (i == 'A'):
		print('T', end="")
	elif (i == 'C'):
		print('G', end="")
	elif (i == 'G'):
		print('C', end="")
	elif (i == 'T'):
		print('A', end="")
print("")

# Close files to end program
dnaSequence.close()