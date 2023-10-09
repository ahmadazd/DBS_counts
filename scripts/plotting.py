import pandas as pd
import os
import argparse
from time import time
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(prog='plotting.py', formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-f', '--file', help='path for the merged normalised counts file', type=str, required=True)
parser.add_argument('-o', '--output', help='output path for plot', type=str, required=True)
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


def upload_count_file(counts_file):
    """
     upload files into dataframes
     :param counts_file: the path for the file
     :returns the dataframe
      """
    counts_df = pd.read_csv(counts_file, sep='\t', names=['sample_id', 'counts'])
    return  counts_df

def plot(df):
    """
     Plotting dataframe
     :param df: the dataframe
     :returns the plot
      """
    plt.figure(figsize=(14, 8))
    plt.bar(df['sample_id'], df['counts'])
    plt.xlabel('Sample id', fontsize=12)
    plt.ylabel('Normalised Counts', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(f"{args.output}/break_counts_plot.png",dpi=400)



@timer
def plotting_process():
    """
         The Main Function
          """
    counts_df = upload_count_file(args.file)
    plot(counts_df)


#####################################################

#                 MAIN                               #

#####################################################

if __name__ == '__main__':
    plotting_process()
