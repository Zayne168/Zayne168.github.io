import pybedtools
import math
import random
#Please install pybedtools using pip install pybedtools in remote env!!

#https://daler.github.io/pybedtools/

def FastaToText(fasta, out_file):
    with open(fasta.seqfn) as f, open(out_file, "w") as out:
        for line in f:
            if line.startswith(">"):
                continue
            out.write(line.strip().lower() + "\n")



myFile1 = "dataIN/ENCFF306FTN.bed"

myReferenceGenome = "/users/zbonner/reference/hg38.fa.fai"
myFasta = "/users/zbonner/reference/hg38.fa"
#adjust directory and file names as necessary :)
#myData = pybedtools.BedTool(myFile)
myGenome = "hg38.genome"
intervalLengths = []
maxLength = 25500

out1 = "dataOUT/bpositive.txt"
out2 = "dataOUT/bnegative.txt"
for file in [myFile1]:
    with open(file) as f:
        for line in f:
            cols = line.strip().split()
            intervalLengths.append(int(cols[2]) - int(cols[1]))

#taking the avg length of each row. my '150' or cropping length is 5% less than the avg interval length
#that feels logical
avg = sum(intervalLengths)/len(intervalLengths)
#print(avg)
avg = avg-(avg*0.05)
avg = math.floor(avg)
avg = 197 # I am the laziest human in the world and hardcoded the avg from the 5 original files
print(avg)

#I am creating a temporary genome file to use with pybedtools
with open(myReferenceGenome) as input, open(myGenome, "w") as output:
    for line in input:
        chrom, length = line.strip().split("\t")[:2]
        output.write(f"{chrom}\t{length}\n")

#combine files
beds = [pybedtools.BedTool(f) for f in [myFile1]]

myData = beds[0]
for b in beds[1:]:
    myData = myData.cat(b, postmerge=False)
myData = myData.sort()
myNegativeData = myData.complement(g=myGenome)
myNegativeTuples = []
myTuples = []
#for i, interval in enumerate(myInvertedData):
#    if i == 5:
#        break
#    print(interval)

#creating tuples for each row. {chrname,start,end}
for i in myData:
    start = i.start
    end = i.end
    l = end - start
    #print(l)
    if l < avg:
        continue
        #if length < avg, skip
    while start + avg <= end:
        myTuples.append((i.chrom, start, start + avg))
        start += avg

for i in myNegativeData:
    start = i.start
    end = i.end
    l = end - start
    #print(l)
    if l < avg:
        continue
        #if length < avg, skip
    while start + avg <= end:
        myNegativeTuples.append((i.chrom, start, start + avg))
        start += avg

#grab random samples/tuples (25k of each)
if len(myTuples) > maxLength:
    myTuples = random.sample(myTuples, maxLength)
myNegativeTuples = random.sample(myNegativeTuples, len(myTuples))


#start output formatting
plusBT = pybedtools.BedTool(myTuples)
minusBT = pybedtools.BedTool(myNegativeTuples)

fastaPositive = plusBT.sequence(fi=myFasta)
fastaNegative = minusBT.sequence(fi=myFasta)

FastaToText(fastaPositive, out1)
FastaToText(fastaNegative, out2)
print("Success probably!")



#with open(out1, "w") as f:
#    for chrom, start, end in myTuples:
#        f.write(f"{chrom}\t{start}\t{end}\n")
#with open(out2, "w") as f:
#    for chrom, start, end in myNegativeTuples:
#        f.write(f"{chrom}\t{start}\t{end}\n")
#perform  "wc -l *file*" in the terminal to check the lengths and then compare
#   (compare n vs m, in reference to inclass notes) 