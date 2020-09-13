#! usr/bin/env python3.7

import sys
import fileinput

# pointMutations.py is a Python3.7 Script that takes a file from command line arguments
# Prints the output to Standard Out.

# Written by Marcus W. on Septemeber 13, 2020

# Welcome to Point Mutation hunting in DNA Python 3.7 Program
# This program takes a .txt file of DNA nucleotides (A,T,C,G).

# Assign the text file from the command line to a variable
seq_File = sys.argv[1]

# Open the text or .fasta file
dnaSequence = open(seq_File)

# Initialize variables
countMutation = 0
loop = 0

# Read the lines of the text or fasta file in. Assign to the first Sequence line
splitFile = dnaSequence.readlines()
dnaSeq1 = splitFile[0]
print("dnaSeq1 contains: " + dnaSeq1)

# Read the next lines of the text or fasta file into the second sequence line
dnaSeq2 = splitFile[1]
print("dnaSeq2 contains: " + dnaSeq2)

# Get the length of each sequence and assign to a variable for the loop length. This is an extra step.
seq1Length = len(dnaSeq1)
seq2Length = len(dnaSeq2)

# Loop through sequence one and compare to sequence two. If different, record difference.
while seq1Length > 0:
    print("The loop count is: {0} amd the countMutation is {1}".format(loop, countMutation))
    if dnaSeq1[loop] != dnaSeq2[loop]:
        countMutation += 1
    seq1Length -= 1
    loop += 1

# Print the final number of mutations.
print("The number of mutations aka the Hamming distance is: {0}".format(countMutation))

# Close files to end program
dnaSequence.close()