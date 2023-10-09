#!/usr/bin/env nextflow

nextflow.enable.dsl=2 

process FILTERING_BREAKS{
	tag "filtering_breaks"                  
	label 'default'                

input:
	path breaks_file
	path output_dir

output:
	path "$output_dir/${breaks_file.baseName}.filtered.bed", emit : filtered_output

script:
	"""
	filtering_reads -f $breaks_file -o $PWD/$output_dir
	"""

}

// This section without any function, its only for debugging or running the module by itself 
workflow {
	breaks_file = file(params.breaks_file).toString()
	breaks = Channel.fromPath( "${breaks_file}/*.breakends.bed")
	output_dir = file(params.output_dir).toString()
	breaks.view().each { breaks_file ->
        FILTERING_BREAKS(breaks_file, output_dir)
	}

}
