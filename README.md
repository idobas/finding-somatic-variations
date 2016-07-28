## finding-somatic-variations
This repository contains scripts usable for doing the entire variant finding process with GATK.

### Requirements

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
	  
3) You need to have a user in orchestra harvard cluster system.


### How to run

Variant calling stage: You first need to put the path to all of your bam files in the runVarCalling script. Once this is set up
you can run it and wait for the results to return (could take some time). Note that some paths need to be altered from the existing 
scripts in order for them to work with your directories. Next, you will need to run the combineVar script, and then the genotypeGVCFS script,
to get the raw variants file.

Varient recalibration stage: Once you have all of the output ready from the variant calling stage, you can run the scripts for variant 
recalibration. Activate these at the following order: snpRecalibrationModel.sh, recalibrateSNPs.sh, indelRecalibrationModel.sh, recalibrateINDELs.sh.
Finally you will get a recal.variants.vcf file.

Final filtering: That stage is our addition relevant only to this project - it filters the variants to leave only the ones that have GT of 0/0 and 
other than 0/0, and also have 99/99 in the GQ. The filtering script is called filteringByGTnGQ.py.

### Final Filtering Script
- Written in python
- Input a vcf file
- Output a txt file that contain the following:
  - Variants filter by GT and GQ arrange by the number of brains we found the current variant
  - The total number of variant 
  - number of variant we found in each brain
  - a list of all the variant we found in each chromosomes (arrange by chromosomes names)
  - a "bucket-list" that conatin the number of variant we found in each bucket (size of one bucket 1 million Nucleic acids)
