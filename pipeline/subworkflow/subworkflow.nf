// See the NOTICE file distributed with this work for additional information
// regarding copyright ownership.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Import modules/subworkflows
include { FILTERING_BREAKS } from '../modules/filtering_breaks.nf'
include { INTERSECTING_BREAKS } from '../modules/intersect_breaks.nf'
include { NORMALISE_COUNTS } from '../modules/normalise_counts.nf'
include {PLOTTING} from '../modules/plotting.nf'

workflow subworkflow { 
    take:
        breaks_file
	    output_dir
        treated_file


    main:

        //breaks_file = file(params.breaks_file).toString()
        breaks = Channel.fromPath( "breaks/*.breakends.bed")
        output_dir = file(params.output_dir).toString()
        breaks.view().each { breaks_file ->
            FILTERING_BREAKS(breaks_file, output_dir)
        }

        //filtered_file = file(FILTERING_BREAKS.out.filtered_output).toString()
        filtered_breaks = Channel.fromPath( "output/*.breakends.filtered.bed")
        output_dir = file(params.output_dir).toString()
        treated_file = file(params.treated_file).toString()
        filtered_breaks.view().each { filtered_file ->
            INTERSECTING_BREAKS(FILTERING_BREAKS.out.filtered_output, treated_file, output_dir)
	    }
 
        //intersected_file = file(INTERSECTING_BREAKS.out.intersect_output).toString()
        intersected_breaks = Channel.fromPath( "output/*.breakends.intersected.bed")

        output_dir = file(params.output_dir).toString()
        initial_file_path = file(params.breaks_file).toString()
        println initial_file_path

        intersected_breaks.view().each { intersected_file ->
            NORMALISE_COUNTS(INTERSECTING_BREAKS.out.intersect_output, initial_file_path, output_dir)
        }

        output_dir = file(params.output_dir).toString()

	    PLOTTING(NORMALISE_COUNTS.out.break_counts, output_dir)

}

// This section without any function, its only for debugging or running the subworkflow by itself 
workflow {
    subworkflow(params.breaks_file, params.output_dir, params.treated_file)
}
