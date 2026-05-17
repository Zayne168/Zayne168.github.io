# Before going further: I referenced "https://github.com/Zayne168/Zayne168.github.io/blob/main/College/sc/spellCheck.html"
# in making this project. We had to do something similar in 340, so I followed the concepts of that project.
# It is in JavaScript so that Github Pages can run it client-side, and I am doing this project in Python.
# I am only following the concepts from my prior project regarding how to perform sequence alignment and matrix management
import numpy as np

def global_align():
	lenSeq1 = len(sequence1)
	lenSeq2	= len(sequence2)
	rowHolder = lenSeq1 
	colHolder = lenSeq2
	alignedSeq1 = ""
	alignedSeq2 = ""
	opt = []

	#OPT matrix initialized as all 0's
	for z in range(lenSeq1+1):
		opt.append([0]*(lenSeq2+1))

	#put in the gap penalties
	for i in range(1, lenSeq1 + 1):
		opt[i][0] = opt[i-1][0] + gapPen
	for j in range(1, lenSeq2 + 1):
		opt[0][j] = opt[0][j-1] + gapPen
	

	#fill in the score
	#diagonal=d, vertical=v, horizontal=h
	for i in range(1,lenSeq1 + 1):
		for j in range(1,lenSeq2+ 1):
			d = opt[i-1][j-1] + subMat[(sequence1[i-1], sequence2[j-1])]
			v = opt[i-1][j] + gapPen
			h = opt[i][j-1] + gapPen
			opt[i][j] = max(d,v,h)
				#find the optimal next step and apply it
				#this system is very similar to the method in my github link. The most notable difference is that
				#in 340, we went with the smallest penalty value as the most optimal.

	#print OPT matrix
	for i in opt:
		print(i)


	



	#traceback loop
	#row and col Holders hold the current position
	while rowHolder > 0 or colHolder > 0:
		if(rowHolder > 0 and colHolder > 0 and opt[rowHolder][colHolder] == opt[rowHolder-1][colHolder-1] + subMat[(sequence1[rowHolder-1], sequence2[colHolder-1])]):
			#if(diagonal is best fit)
			alignedSeq1 = sequence1[rowHolder-1] + alignedSeq1
			alignedSeq2 = sequence2[colHolder-1] + alignedSeq2
			rowHolder -=1
			colHolder -=1
		elif rowHolder > 0 and opt[rowHolder][colHolder] == opt[rowHolder-1][colHolder] + gapPen:
			#if(vertical is best fit)
			alignedSeq1 = sequence1[rowHolder-1] + alignedSeq1
			alignedSeq2 = "-" + alignedSeq2
			rowHolder -= 1
		else:
			#else(horizontal is best fit)
			alignedSeq1 = "-" + alignedSeq1
			alignedSeq2 = sequence2[colHolder-1] + alignedSeq2
			colHolder -=1
		
	#output
	print("OPT alignment score: ", opt[lenSeq1][lenSeq2])
	print("Alignment 1:", alignedSeq1)
	print("Alignment 2:", alignedSeq2)



#######################################################################

def semiglobal_align():
	lenSeq1 = len(sequence1)
	lenSeq2	= len(sequence2)
	rowHolder = lenSeq1 
	colHolder = lenSeq2
	alignedSeq1 = ""
	alignedSeq2 = ""
	maxScore = -800756759
	maxIndex = -800756759
	opt = []

	#OPT matrix initialized as all 0's
	for z in range(lenSeq1+1):
		opt.append([0]*(lenSeq2+1))

	#not inserting gap pens here, unlike global :)

	for i in range(1,lenSeq1 + 1):
		for j in range(1,lenSeq2+ 1):
			d = opt[i-1][j-1] + subMat[(sequence1[i-1], sequence2[j-1])]
			v = opt[i-1][j] + gapPen
			h = opt[i][j-1] + gapPen
			opt[i][j] = max(d,v,h)


	for i in opt:
		print(i)

	#finds the starting point 
	#row max is the max score in the last row
	#col max is the max score in the last column
	#below is finding each of those

	for i in range(lenSeq2+1):
		if opt[lenSeq1][i] > maxScore:
			maxScore = opt[lenSeq1][i]
			maxIndex = i

	rowMax = (maxScore,maxIndex)
	maxScore = -800756759
	maxIndex = -800756759
	

	for i in range(lenSeq1+1):
		if opt[i][lenSeq2] > maxScore:
			maxScore = opt[i][lenSeq2]
			maxIndex = i
	colMax = (maxScore,maxIndex)

	#find the max value between the 2, this is the starting point.
	if rowMax[0] >= colMax[0]:
		rowHolder = lenSeq1
		colHolder = rowMax[1]
	else:
		rowHolder = colMax[1]
		colHolder = lenSeq2






	#traceback loop
	#row and col Holders hold the current position
	while rowHolder > 0 or colHolder > 0:
		if(rowHolder > 0 and colHolder > 0 and opt[rowHolder][colHolder] == opt[rowHolder-1][colHolder-1] + subMat[(sequence1[rowHolder-1], sequence2[colHolder-1])]):
			#if(diagonal is best fit)
			alignedSeq1 = sequence1[rowHolder-1] + alignedSeq1
			alignedSeq2 = sequence2[colHolder-1] + alignedSeq2
			rowHolder -=1
			colHolder -=1
		elif rowHolder > 0 and opt[rowHolder][colHolder] == opt[rowHolder-1][colHolder] + gapPen:
			#if(vertical is best fit)
			alignedSeq1 = sequence1[rowHolder-1] + alignedSeq1
			alignedSeq2 = "-" + alignedSeq2
			rowHolder -= 1
		else:
			#else(horizontal is best fit)
			alignedSeq1 = "-" + alignedSeq1
			alignedSeq2 = sequence2[colHolder-1] + alignedSeq2
			colHolder -=1
		

	#output
	print("OPT alignment score: ", max(rowMax[0], colMax[0]))
	print("Alignment 1:", alignedSeq1)
	print("Alignment 2:", alignedSeq2)



########################################################################

def local_align():
	lenSeq1 = len(sequence1)
	lenSeq2	= len(sequence2)
	rowHolder = lenSeq1 
	colHolder = lenSeq2
	alignedSeq1 = ""
	alignedSeq2 = ""
	maxScore = -800756759
	opt = []

	#OPT matrix initialized as all 0's
	for z in range(lenSeq1+1):
		opt.append([0]*(lenSeq2+1))

	#opt matrix -> filling in scores
	for i in range(1,lenSeq1 + 1):
		for j in range(1,lenSeq2+ 1):
			d = opt[i-1][j-1] + subMat[(sequence1[i-1], sequence2[j-1])]
			v = opt[i-1][j] + gapPen
			h = opt[i][j-1] + gapPen
			opt[i][j] = max(0, d,v,h)
			if opt[i][j] > maxScore:
				maxScore = opt[i][j]
				startPosition = (i,j)
				#the main difference here is that there is no negatives, 
				#and the biggest score is saved for the starting point of alignment
	
	for i in opt:
		print(i)


	#traceback loop
	#row and col Holders hold the current position
	rowHolder, colHolder = startPosition
	while (rowHolder > 0 or colHolder > 0) and opt[rowHolder][colHolder] != 0:
		if(rowHolder > 0 and colHolder > 0 and opt[rowHolder][colHolder] == opt[rowHolder-1][colHolder-1] + subMat[(sequence1[rowHolder-1], sequence2[colHolder-1])]):
			#if(diagonal is best fit)
			alignedSeq1 = sequence1[rowHolder-1] + alignedSeq1
			alignedSeq2 = sequence2[colHolder-1] + alignedSeq2
			rowHolder -=1
			colHolder -=1
		elif rowHolder > 0 and opt[rowHolder][colHolder] == opt[rowHolder-1][colHolder] + gapPen:
			#if(vertical is best fit)
			alignedSeq1 = sequence1[rowHolder-1] + alignedSeq1
			alignedSeq2 = "-" + alignedSeq2
			rowHolder -= 1
		else:
			#else(horizontal is best fit)
			alignedSeq1 = "-" + alignedSeq1
			alignedSeq2 = sequence2[colHolder-1] + alignedSeq2
			colHolder -=1
		
	#output
	print("OPT alignment score: ", maxScore)
	print("Alignment 1:", alignedSeq1)
	print("Alignment 2:", alignedSeq2)



######################################################
#Start of Main()

seqFile1 = input("Name of sequence file 1: ")
seqFile2 = input("Name of sequence file 2: ")
subMatFile = input("Name of submatrix file: ")
alignType = int(input("Type of alignment (single integer please: 1=global, 2=semi-global, 3=local): "))
gapPen = int(input("Gap penalty to be used: "))
subMat = {}

with open(seqFile1, 'r') as file:
    file.readline()
    sequence1 = file.readline().strip()

with open(seqFile2, 'r') as file:
    file.readline()
    sequence2 = file.readline().strip()

		#Both sequence files assume that the first line is a title (and is  thus skipped), 
		#	and the second line is the sequence


with open(subMatFile, 'r') as file:
	next(file)		#skip line 1
	
	aminoAcidOrder = next(file).strip().split(',')
		#second line contains the order of the AA in the matrix

	#i = row index, j = column index == (i,j)
	#rest of vars should be self explanitory

	for i, line in enumerate(file):
		scoresPerLine = list(map(int, line.strip().split(',')))
		for j,score in enumerate(scoresPerLine):
			subMat[(aminoAcidOrder[i],aminoAcidOrder[j])]=score
	#this loop indexes through each line, and matches each score to a spot on the created submatrix

#This is error checking. It is horrendous to actually read,
#	but it prints out how everything is aligned and the 2 sequences read int
#for i, value in subMat.items():
#    print(f"{i}: {value}")
#print(sequence1)
#print(sequence2)


if alignType == 1:
	global_align()
elif alignType == 2:
	semiglobal_align()
elif alignType == 3:
	local_align()
else:
	print("You did not input 1, 2, or 3 for the alignment type.")



