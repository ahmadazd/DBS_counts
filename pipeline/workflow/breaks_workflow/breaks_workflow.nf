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
nextflow.enable.dsl=2

//default params
params.help = false

// mandatory params
params.breaks_file = null
params.output_dir = null
params.treated_file = null


// Print usage
def helpMessage() {
  log.info """
        Usage:
        The typical command for running the pipeline is as follows:
        nextflow run pipeline/workflow/breaks_workflow/breaks_workflow.nf


        Mandatory arguments:
        --breaks_file                 The path for the breaks bed files directory (Retrieved from the nextflow.config file)
        --output_dir                  The path for the output directory (Retrieved from the nextflow.config file)
        --treated_file                The path for the AsiSI_sites bed file  (Retrieved from the nextflow.config file)

        Optional arguments:
        --help                         This usage statement.
        """
}

// Show help message
if (params.help) {
    helpMessage()
    exit 0
}

assert params.breaks_file, "Parameter 'breaks_file' is not specified"
assert params.output_dir, "Parameter 'output_dir' is not specified"
assert params.treated_file, "Parameter 'treated_file' is not specified"

// Import modules/subworkflows
include { subworkflow } from '../../subworkflow/subworkflow.nf'

// Run main workflow
workflow {
    main:
    subworkflow(params.breaks_file, params.output_dir, params.treated_file)
}