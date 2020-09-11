#! usr/bin/env python3.7

import sys
import fileinput

# DNA_Count Python3.7 Script that takes a file from command line arguments 
# and counts the number of A, C, G, T's. Than Prints them.

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
dna_File = open("DNA_SampleDataset.txt", 'r')

# Loop to parse the muilti-fasta file inside a loop to go through gene name text file, increasing each integer as it is spotted.
for lines in dna_File:
	varA = varA + lines.count("A")
	varC = varC + lines.count("C")
	varG = varG + lines.count("G")
	varT = varT + lines.count("T")

# Alternatively, you could read the whole file into one variable and use .count() method.
# full_Sequence = dna_File.readline().rstrip()
# varA = full_Sequence.count("A")
# varC = full_Sequence.count("C")
# varG = full_Sequence.count("G")
# varT = full_Sequence.count("T")

# Print the Results
print("A = {0} C = {1} G = {2} T = {3}".format(varA, varC, varG, varT))

# Close files to end program
dna_File.close()