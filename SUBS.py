#! usr/bin/env python3.7

import sys
import fileinput

# DNA_Count Python3.7 Script that takes a file from command line arguments
# Prints the output to Standard Out.

# Written by Marcus W. on September 15, 2020

# Welcome to Motif Hunting in DNA Python 3.7 Program
# This program takes two .txt files. One of a DNA nucleotides (A,T,C,G) and the other of a motif file.
# The file than takes the motif and records all the starting nucleotide locations in the file.

# Assign the command line arguements to variables.
seq_File = sys.argv[1]
print("The file argument is " + seq_File)

motif_File = sys.argv[2]
print("The file argument is " + motif_File)

# Open the muilti-fasta file
dnaSequence = open(seq_File)
dnaMotif = open(motif_File)

# Loop through dnaMotif file and store in String.
lines_dnaMotif = dnaMotif.readlines()
motifStr = ""

# Loop through the
for lined_dnaMotif in lines_dnaMotif:
	for charMotif in lined_dnaMotif:
		motifStr = motifStr+charMotif

motifStr = motifStr.rstrip('\n')

# Loop through dnaSequence file and store to string.
# to parse the muilti-fasta file inside a loop to go through gene name text file
lines_dnaSeq = dnaSequence.readlines()
dnaSeqStr = ""

for lined_dnaSeq in lines_dnaSeq:
	for charSeq in lined_dnaSeq:
		dnaSeqStr = dnaSeqStr+charSeq

# Get the length and initialize the motif count variable.
countMotifFound = 0
motifLength = len(motifStr)
seqLength = len(dnaSeqStr)

# Initialize Variables
found = []
index = 0
indexEnd = motifLength
y = 0

# Loop through the index and find where the motif is within the sequence and record it.
#.find() motifStr in dnaSeqStr
while index < seqLength:
	indexEnd = index + motifLength
	x = dnaSeqStr.find(motifStr, index, indexEnd)
	print("The index is {0} and the indexEnd is {1}".format(index, indexEnd))
	if x > y:
		countMotifFound += 1
		found.append(x+1)
		print(x)
	index += 1

# Print the results.
print("There are {0} motifs at {1}".format(countMotifFound, index))
print(found)

# Close files to end program
dnaSequence.close()
dnaMotif.close()