import pandas as pd
import os
import argparse
from time import time


parser = argparse.ArgumentParser(prog='normalise_counts.py', formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-f', '--file', help='path for the intersected output bed file', type=str, required=True)
parser.add_argument('-s', '--orginalSample', help='path for the original sample bed file', type=str, required=True)
parser.add_argument('-o', '--output', help='output path for the normalised counts file', type=str, required=True)
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


def upload_bed_files(intersected_read_file, initial_breaks):
    """
     upload files into dataframes
     :param intersected_read_file, initial_breaks: the path for the files
     :returns  dataframes of the intersected_read and initial_breaks
      """
    if os.stat(intersected_read_file).st_size == 0:
        intersected_read_df = pd.DataFrame()
    else:
        intersected_read_df = pd.read_csv(intersected_read_file, sep='\t', header=None)

    initial_breaks_df = pd.read_csv(initial_breaks, sep='\t', header=None)
    return  intersected_read_df, initial_breaks_df

def sum_normalise(intersected_read_df, initial_breaks_df):
    """
     sum and normalise the dataframe against the initial breaks counts and print them into a single file
     :param intersected_read_df, initial_breaks_df: dataframes of the intersected_read and initial_breaks
     :returns  normalised Counts
      """
    break_counts = len(intersected_read_df)
    if break_counts != 0:
        total_breaks_counts = len(initial_breaks_df)
        normalise_count = break_counts/(total_breaks_counts/1000)
    else:
        normalise_count = 0
    print(normalise_count)

    with open(f"{args.output}/normalised_counts.txt", 'a') as f:
        f.write(os.path.basename(args.orginalSample).strip('.breakends.bed') + '\t' + str(normalise_count) + '\n')



@timer
def breaks_normalising_process():
    """
         The Main Function
          """
    breaks_df = upload_bed_files(args.file, args.orginalSample)
    sum_normalise(breaks_df[0], breaks_df[1])


#####################################################

#                 MAIN                               #

#####################################################

if __name__ == '__main__':
    breaks_normalising_process()
