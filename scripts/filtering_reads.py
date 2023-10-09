
import pandas as pd
import os
import argparse
from time import time


parser = argparse.ArgumentParser(prog='filtering_reads.py', formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-f', '--file', help='path for the bed file', type=str, required=True)
parser.add_argument('-o', '--output', help='output path for the filtered bed file', type=str, required=True)
args = parser.parse_args()

def timer(function):
    """
     Execution time of a function object
     :param function: function name
     :returns the time the function spent
      """
    def wrapper(*parameters):
        t1 = time()
        result = function(*parameters)
        t2 = time()
        print(f'Process {function.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrapper

def create_outdir(output):
    """
     create a directory
     :param output: the path for the output directory and the name of the directory to be created
     :returns the path and the name of the directory that been created
      """
    outdir = f"{output}"
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    return outdir

def upload_bed_files(file):
    """
     upload files into dataframes
     :param file: the path for the files
     :returns  dataframes of the initial_breaks files
      """
    bed_file_df = pd.read_csv(file, sep='\t', header=None)
    return  bed_file_df

def filter_bed_file(bed_df):
    """
     filter the dataframe to remove any break with a score less than 30
     :param bed_df: breaks dataframe
     :returns  the filtered files
      """
    filtered_bed_df = bed_df[bed_df.apply(lambda x: x[4] >= 30, axis=1)]

    outdir = create_outdir(args.output)

    filtered_bed_df.to_csv(f"{outdir}/{os.path.basename(args.file).strip('.bed')}.filtered.bed", sep='\t', index=False, header=False)

@timer
def reads_filtering_process():
    """
         The Main Function
          """
    bed_df = upload_bed_files(args.file)
    filtered_bed_df = filter_bed_file(bed_df)

#####################################################

#                 MAIN                               #

#####################################################

if __name__ == '__main__':
    reads_filtering_process()


