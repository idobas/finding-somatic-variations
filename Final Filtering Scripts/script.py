#!/usr/bin/python

import sys

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

#will always close the file
with open(sys.argv[1] , 'r') as f:
	read_data = f.read()

startLoc	= read_data.find("#CHROM")

varTable	= read_data[startLoc:]

varLineList 	= varTable.split('\n')

result		= "\tCHROM\tPOS\tID\tREF\tALT\tQUAL\t\tFILTER"

num = 0

# for each line in table
for i in range(1, len(varLineList)):
	

	varLineColList	= varLineList[i].split('\t')
	addLine = False

	if len(varLineColList) < COL_VALUE.get("SIZE") or varLineColList[COL_VALUE.get("FILTER")] != "PASS" :
		continue
	
	#print variant info
	varLineInfo = "(" + `i` + ")\t"
	for j in range(0 , COL_VALUE.get("INFO")):
		varLineInfo += varLineColList[j] + "\t"
	temp = "\n" + varLineInfo + "\n"
	
	#print (1,1|0) , (0,1|0)
	temp  += "\t\tGT_cer , GT_pfx \t AD_cer , AD_pfx \t GQ_cer , GQ_pfx \n"
        for j in xrange(COL_VALUE.get("FORMAT") + 1, COL_VALUE.get("SIZE"), 2):
               	cerInfo = varLineColList[j].split(":")
               	pfxInfo = varLineColList[j+1].split(":")
               	if      cerInfo[0] != pfxInfo[0] and (cerInfo[0]=="0/0" or pfxInfo[0]=="0/0") and (cerInfo[0]!="./." and pfxInfo[0]!="./."):
                       	temp += "\t" + COL_NAME.get(j) + ":\t" + cerInfo[0] + " , " + pfxInfo[0] + "\t"+ cerInfo[1] + " , " + pfxInfo[1] + "\t" + cerInfo[3] + " , " + pfxInfo[3]  + "\n"
                   	addLine = True
        if addLine :
                result += temp
                num = num + 1
	
result += "\n\nnum = " + `num` + "\n\n"
#will always close the file
with open('res' , 'w') as f:
	f.write(result)

sys.exit()

