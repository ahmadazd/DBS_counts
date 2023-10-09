#!/usr/bin/env nextflow

nextflow.enable.dsl=2 

process INTERSECTING_BREAKS{
	tag "intersect_breaks"                  
	label 'default'                

input:
	path filtered_file
	path treated_file
	path output_dir

output:
	path "$output_dir/${filtered_file.baseName.minus('.filtered')}.intersected.bed", emit : intersect_output

script:
	"""
	intersect_breaks -f $filtered_file -a $treated_file  -o $PWD/$output_dir
	"""

}

// This section without any function, its only for debugging or running the module by itself 
workflow {
	filtered_file = file(params.filtered_file).toString()
	filtered_breaks = Channel.fromPath( "${filtered_file}/*.breakends.filtered.bed")
	output_dir = file(params.output_dir).toString()
	treated_file = file(params.treated_file).toString()
	filtered_breaks.view().each { filtered_file ->
        INTERSECTING_BREAKS(filtered_file, treated_file, output_dir)
	}

}
