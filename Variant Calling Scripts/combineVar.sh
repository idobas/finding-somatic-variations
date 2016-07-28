#!/bin/bash

myPath="/n/scratch2/idoDan/vcfFiles/"

module load dev/java/jdk1.6
module load seq/gatk/3.6


bsub -e errfile -q short  -W 12:0 -R "rusage[mem=64000]"  java -Xmx64g -jar GenomeAnalysisTK.jar -R /n/scratch2/idoDan/genome.fa -T CombineGVCFs --variant $myPath"1349_cer_7.raw.snps.indels.g.vcf" --variant $myPath"4231_pfx_3.raw.snps.indels.g.vcf" --variant $myPath"4899_cer_7.raw.snps.indels.g.vcf" --variant $myPath"5027_pfx_3.raw.snps.indels.g.vcf" --variant $myPath"1349_pfx_7.raw.snps.indels.g.vcf" --variant $myPath"4671_cer_5.raw.snps.indels.g.vcf" --variant $myPath"4899_pfx_7.raw.snps.indels.g.vcf" --variant $myPath"5115_cer_9.raw.snps.indels.g.vcf" --variant $myPath"1638_cer_7.raw.snps.indels.g.vcf" --variant $myPath"4671_pfx_5.raw.snps.indels.g.vcf" --variant $myPath"4999_cer_9.raw.snps.indels.g.vcf" --variant $myPath"5115_pfx_5.raw.snps.indels.g.vcf" --variant $myPath"1638_pfx_5.raw.snps.indels.g.vcf" --variant $myPath"4721_cer_7.raw.snps.indels.g.vcf" --variant $myPath"4999_pfx_3.raw.snps.indels.g.vcf" --variant $myPath"5144M_cer_9.raw.snps.indels.g.vcf" --variant $myPath"4231_cer_5.raw.snps.indels.g.vcf" --variant $myPath"4721_pfx_5.raw.snps.indels.g.vcf" --variant $myPath"5027_cer_7.raw.snps.indels.g.vcf" --variant $myPath"5144M_pfx_1.raw.snps.indels.g.vcf" -o all.g.vcf


