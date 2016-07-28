#!/bin/bash

myPath="/n/scratch2/idoDan/"

[ -e errfile ] && rm errfile

module load dev/java/jdk1.6
module load seq/gatk/3.6
module load stats/R/3.3.1
#R '.libsPaths();'
#mkdir ~/local/R_libs
#Rscript -e 'install.packages("ggplot2", repos="http://cran.r-project.org", lib="~/local/R_libs/")'

[ ! -e $myPath"genome.fa.fai" ] && echo "cant file file: genome.fa.fai"		&& exit

[ ! -e $myPath"genome.fa" ]	&& echo "cant file file: genome.fa" 		&& exit	

[ ! -e $myPath"genome.dict" ] 	&& echo "cant find  file: genome.dict" 		&& exit

[ ! -e GenomeAnalysisTK.jar ] 	&& echo "can't find file: GenomeAnalysisTK.jar" && exit

bsub -o outfile -e errfile -q priority  -W 12:0 -R "rusage[mem=64000]" java -Xmx64g -jar GenomeAnalysisTK.jar -T VariantRecalibrator -R $myPath"genome.fa" -input raw_variants.vcf -resource:hapmap,known=false,training=true,truth=true,prior=15.0 hapmap_3.3.b37chr.vcf -resource:omni,known=false,training=true,truth=true,prior=12.0 1000G_omni2.5.b37chr.vcf -resource:1000G,known=false,training=true,truth=false,prior=10.0 1000G_phase1.snps.high_confidence.b37chr.vcf -resource:dbsnp,known=true,training=false,truth=false,prior=2.0 dbsnp_138.b37chr.vcf -an DP -an QD -an FS -an SOR  -an MQRankSum  -an ReadPosRankSum -mode SNP -tranche 100.0 -tranche 99.9 -tranche 99.0 -tranche 90.0 -recalFile recalibrate_SNP.recal -tranchesFile recalibrate_SNP.tranches -rscriptFile recalibrate_SNP_plots.R


exit

