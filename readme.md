
# DSBs counts Task

The workflows includes the following process:
-  **Filtering Breaks:** Filter out reads that have a mapping quality of < 30.
-  **Intersect Breaks:** Intersect each sample break bed file with the AsiSI site bed file.
-  **Normalise Counts:** Sum and normalise the Break counts and Collect them in a single file.
-  **Counts Plotting:** Plotting the collected counts from all the samples

**OUTPUTS**
All the output files are found in the ``output`` directory.  

Four types of output files and they are as follows:
-  **``Sample*.breakends.filtered.bed``:** Filtering breaks process output
- **``Sample*.breakends.intersected.bed``:** Intersect breaks process output
- **``normalised_counts.txt``:** Normalise counts process output
- **``break_counts_plot.png``:** Graph for the normalised counts 

#### Before Starting
-  **Clone**
``git clone <github repository>``

- **Run the following**
``pip install -e .``

**NOTE:**
``All the parameters are stored in the nextflow.config file`` 

#### Run the Workflow
``nextflow run pipeline/workflow/breaks_workflow/breaks_workflow.nf``

## Questions and the Answers
1.  Which of the samples are likely to be controls or treated?
   
	**Answer**

	**``Control``** : ``Sample1, Sample8, Sample2, Sample6, Sample5, Sample7, Sample4``

	**``Treated``** : ``Sample9, Sample16, Sample10, Sample15, Sample11, Sample14,  Sample12`` 
	
2.  Are there any you are uncertain of?
   
	**Answer**

	``Yes, Sample13, Sample3``
3.  Can you explain the samples in the uncertain group?
   
       **Answer**  

        ``Both Sample 13 and Sample 3 have low intersected break counts (near or under 1 after normalising),
          so this overlap might be just coincidental``  

5.  Of all the possible AsiSI sites described in the chr21_AsiSI_sites.t2t.bed file what is the maximum percentage observed in a single sample?  

       **Answer** : ``14%``
