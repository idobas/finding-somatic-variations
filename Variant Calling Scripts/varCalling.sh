#!/bin/bash

myPath="/n/scratch2/idoDan/"

[ -e errfile ] && rm errfile

module load dev/java/jdk1.6
module load seq/gatk/3.6

[ ! -e $myPath"genome.fa.fai" ] && echo "cant file file: genome.fa.fai"		&& exit

[ ! -e $myPath"genome.fa" ]	&& echo "cant file file: genome.fa" 		&& exit	

[ ! -e $myPath"genome.dict" ] 	&& echo "cant find  file: genome.dict" 		&& exit

[ ! -e GenomeAnalysisTK.jar ] 	&& echo "can't find file: GenomeAnalysisTK.jar" && exit

bsub -o outfile  -e errfile  -q short -W 12:0 -R "rusage[mem=64000]"  java -Xmx64g  -jar GenomeAnalysisTK.jar -T HaplotypeCaller -R $myPath"genome.fa" -I $1 -L $myPath"utils/Broad.human.exome.b37chr.interval_list"  --emitRefConfidence GVCF --variant_index_type LINEAR --variant_index_parameter 128000 --dbsnp dbsnp_138.b37chr.vcf -o $myPath"vcfFiles/"$2".raw.snps.indels.g.vcf"


exit

