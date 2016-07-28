#!/bin/bash

myPath="/n/scratch2/idoDan/"

[ -e errfile ] && rm errfile

module load dev/java/jdk1.6
module load seq/gatk/3.6
module load stats/R/3.3.1
[ ! -e $myPath"genome.fa.fai" ] && echo "cant file file: genome.fa.fai"		&& exit

[ ! -e $myPath"genome.fa" ]	&& echo "cant file file: genome.fa" 		&& exit	

[ ! -e $myPath"genome.dict" ] 	&& echo "cant find  file: genome.dict" 		&& exit

[ ! -e GenomeAnalysisTK.jar ] 	&& echo "can't find file: GenomeAnalysisTK.jar" && exit

bsub -q priority  -o outfile -e errfile -W 12:0 -R "rusage[mem=64000]" java -Xmx64g -jar GenomeAnalysisTK.jar -T VariantRecalibrator -R $myPath"genome.fa" -input recalibrated_snps_raw_indels.vcf -resource:mills,known=true,training=true,truth=true,prior=12.0 Mills_and_1000G_gold_standard.indels.b37chr.vcf -resource:dbsnp,known=true,training=false,truth=false,prior=2.0 dbsnp_138.b37chr.vcf -an DP -an QD -an FS -an SOR  -an MQRankSum  -an ReadPosRankSum --maxGaussians 4  -mode INDEL -tranche 100.0 -tranche 99.9 -tranche 99.0 -tranche 90.0 -recalFile recalibrate_INDEL.recal -tranchesFile recalibrate_INDEL.tranches -rscriptFile recalibrate_INDEL_plots.R


exit

