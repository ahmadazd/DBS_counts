#!/usr/bin/env nextflow

nextflow.enable.dsl=2 

process NORMALISE_COUNTS{
	tag "normalise_breaks_counts"                  
	label 'default'                

input:
	path intersected_file
	path initial_file
	path output_dir

output:
	path "$output_dir/normalised_counts.txt", emit : break_counts

script:
	orignal_samples = "$PWD/${initial_file}/${intersected_file.baseName.minus('.intersected')}.bed"
	"""
	normalise_counts -f $intersected_file -s ${orignal_samples}  -o $PWD/$output_dir
	"""

}

// This section without any function, its only for debugging or running the module by itself 
workflow {
	intersected_file = file(params.intersected_file).toString()
	intersected_breaks = Channel.fromPath( "${intersected_file}/*.breakends.intersected.bed")

	output_dir = file(params.output_dir).toString()
	initial_file_path = file(params.initial_file).toString()

	intersected_breaks.view().each { intersected_file ->
        NORMALISE_COUNTS(intersected_file, initial_file_path, output_dir)
    }

}
