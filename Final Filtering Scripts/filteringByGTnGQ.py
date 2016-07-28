#!/usr/bin/python

import sys

GT = 0
AD = 1
DP = 2
GQ = 3
PL = 4

COL_VALUE = {
	"CHROM"		: 0,
	"POS"     	: 1,
	"ID"      	: 2,
	"REF" 		: 3, 
	"ALT"     	: 4,
	"QUAL"   	: 5, 
	"FILTER"    	: 6,
	"INFO" 		: 7,
	"FORMAT"	: 8,
	"SIZE"		: 28,
}

COL_NAME = {
	9	: "1349" ,   
 	11	: "1638" ,
	13	: "4231" ,
	15	: "4671" ,
	17	: "4721" ,
	19	: "4899" ,
	21	: "4999" ,
	23	: "5027" ,
	25	: "5115" ,
	27	: "5144M" ,
}

CHR_LOC = {
	"chr1"	: 0, "chr2"   : 1, "chr3"   : 2, "chr4"   : 3, "chr5"   : 4, "chr6"   : 5, "chr7"   : 6,  "chr8"   : 7,  "chr9"   : 8, "chr10"  : 9,  "chr11"  : 10,
        "chr12"	: 11, "chr13" : 12, "chr14" : 13, "chr15" : 14, "chr16" : 15, "chr17" : 16, "chr18" : 17,  "chr19" : 18,  "chr20" : 19, "chr21" : 20,  "chr22" : 21,
        "chrM"  : 22, "chrX"  : 23, "chrY"  : 24, 
}

CHR_LEN = {
	"chrM" 	:16571 , "chr2" :243199373 , "chr3" :198022430 , "chr4" :191154276 , "chr5" :180915260 , "chr6" :171115067 , "chr8" :146364022 , "chr9" :141213431 ,
	"chr10" :135534747 , "chr11"   :135006516 , "chr12"   :133851895 , "chr13"   :115169878 , "chr14"   :107349540 , "chr15"   :102531392 , "chr16"   :90354753 ,
	"chr17" :81195210 , "chr18"   :78077248 , "chr19"   :59128983 , "chr20"   :63025520 , "chr21"   :48129895 , "chr22"   :51304566 , "chrX" 	:155270560 ,
	"chrY" 	:59373566 ,
}

varNum = 0
resArrangeByBriansNumArr = ["" for x in range(10)]
brainsNumArr = [ 0 for x in range(10)]
chrArr = [[] for x in range(25) ]

#will always close the file
with open(sys.argv[1] , 'r') as f:
	read_data = f.read()

startLoc	= read_data.find("#CHROM")

varTable	= read_data[startLoc:]

varLineList 	= varTable.split('\n')

result		= "\tCHROM\tPOS\tID\tREF\tALT\tQUAL\t\tFILTER\n"

# for each line in table
for i in range(1, len(varLineList)):
	
	addLine = False
	brainsNum = 0
	varLineColList	= varLineList[i].split('\t')
	tempBrainsNumArr = [ 0 for x in range(10)]

	if len(varLineColList) < COL_VALUE.get("SIZE") or varLineColList[COL_VALUE.get("FILTER")] != "PASS" :
		continue
	
	#variant info
	varLineInfo = "(" + `i` + ")\t"
	for j in range(0 , COL_VALUE.get("INFO")):	
		varLineInfo += varLineColList[j] + "\t"
	temp = "\n" + varLineInfo + "\n"
	
	#filter varint by GT and GQ
	temp  += "\t\tGT_cer  GT_pfx\t\tAD_cer  AD_pfx\t\tGQ_cer  GQ_pfx\n"
        for j in xrange(COL_VALUE.get("FORMAT") + 1, COL_VALUE.get("SIZE"), 2):
               	cerInfo = varLineColList[j].split(":")
               	pfxInfo = varLineColList[j+1].split(":")
		
		if len(cerInfo) <= GQ or len(pfxInfo) <= GQ :
			continue	   		

		if cerInfo[GT] != pfxInfo[GT] and (cerInfo[GT]=="0/0" or pfxInfo[GT]=="0/0") and (cerInfo[GT]!="./." and pfxInfo[GT]!="./."):
			loc = (j - 9) / 2
			tempBrainsNumArr[loc] += 1 
			temp += "\t" + COL_NAME.get(j) + ":"
			temp += "\t" + cerInfo[GT] + " ; " + pfxInfo[GT] + "\t"
			temp += "\t" + cerInfo[AD] + " ; " + pfxInfo[AD] + "\t" 
			temp += "\t" + cerInfo[GQ] + " ; " + pfxInfo[GQ] + "\t\n"
			brainsNum += 1
			if (cerInfo[GQ] == "99" and pfxInfo[GQ] == "99"):
                       		addLine = True
        
	if addLine :
		# save chrom positions 
		chrName = varLineColList[COL_VALUE.get("CHROM")]
		chrLoc  = CHR_LOC.get(chrName)
		chrPos  = varLineColList[COL_VALUE.get("POS")] 
		if len(chrArr[chrLoc]) == 0 :
			chrArr[chrLoc].append(chrName)
		chrArr[chrLoc].append(chrPos)
		
		# save res output
		resArrangeByBriansNumArr[brainsNum-1] += temp	
                # count num of variants
		varNum = varNum + 1
		# count brains num
		for j in range(0,10):
			brainsNumArr[j] += tempBrainsNumArr[j]

for i in range(0,10) :
	result += "--------------------------------------- num of brains = " + `i+1`;
	result += " ---------------------------------------\n"
	result += resArrangeByBriansNumArr[i];
	
result += "\n\nnumber of variants  = " + `varNum` + "\n\n"

brainsNameArr = ["1349" , "1638" , "4231" , "4671" , "4721" , "4899" , "4999" , "5027" , "5115" , "5144M"]
for i in range(0,10):
	result += "brain-"+ brainsNameArr[i] + ": "  + `brainsNumArr[i]` + "\n"

# print variants chromosomes positions
result += "\n\n variants chromosomes positions:\n\n"
for i in range(0,25):
	total = 0
	chrBucket = [ 0 for x in range(300)]
	for j in range(1,len(chrArr[i])):
		loc = int(chrArr[i][j]) / 1000000
		chrBucket[loc] += 1
	result += `chrArr[i]` + "\n"  
	for j in range(0,300):
		if chrBucket[j]>0 : 
			result += `j`+"M:"+`chrBucket[j]`  + "; "
			total += chrBucket[j]
	result += "total = "+ `total`  +"\n\n"

result += "\n"

#will always close the file
with open('filteringResults.txt' , 'w') as f:
	f.write(result)

sys.exit()

