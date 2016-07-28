# finding-somatic-variations
This repository contains scripts usable for doing the entire variant finding process with GATK.

Requirements:
1) You need to have the GATK jar file (https://software.broadinstitute.org/gatk/download/)
2) You also need to have the following files:
      1000G_omni2.5.b37chr.vcf
      1000G_phase1.snps.high_confidence.b37chr.vcf
      dbsnp_138.b37chr.vcf
      hapmap_3.3.b37chr.vcf
      Mills_and_1000G_gold_standard.indels.b37chr.vcf
      A reference file (in our case it was called genome.fa and contained the human genome)
      A dict file (genome.dict) - needs to be in the same folder as genome.fa
      A fai file (genome.fa.fai) - also needs to be in the same folder


