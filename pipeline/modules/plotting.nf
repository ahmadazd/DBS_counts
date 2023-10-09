#!/usr/bin/env nextflow

nextflow.enable.dsl=2 

process PLOTTING{
	tag "plotting"                  
	label 'default'                

input:
	path break_counts
	path output_dir


script:
	"""
	plotting -f ${break_counts} -o $PWD/${output_dir}
	"""

}
// This section without any function, its only for debugging or running the module by itself 
workflow {
	output_dir = file(params.output_dir).toString()
	break_counts = file(params.break_counts).toString()

	PLOTTING_CH = PLOTTING(break_counts, output_dir)
}

