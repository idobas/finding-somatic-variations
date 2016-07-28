#!/bin/bash

myPath="/n/scratch2/idoDan/"

[ -e errfile ] && rm errfile

module load dev/java/jdk1.6
module load seq/gatk/3.6

[ ! -e $myPath"genome.fa.fai" ] && echo "cant file file: genome.fa.fai"		&& exit

[ ! -e $myPath"genome.fa" ]	&& echo "cant file file: genome.fa" 		&& exit	

[ ! -e $myPath"genome.dict" ] 	&& echo "cant find  file: genome.dict" 		&& exit

[ ! -e GenomeAnalysisTK.jar ] 	&& echo "can't find file: GenomeAnalysisTK.jar" && exit

bsub -e errfile -o outfile  -q priority  -W 12:0 -R "rusage[mem=64000]" java -Xmx64g  -jar GenomeAnalysisTK.jar -R $myPath"genome.fa"  -T GenotypeGVCFs --variant all.g.vcf -o raw_variants.vcf


exit

