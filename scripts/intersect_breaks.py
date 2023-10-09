import pandas as pd
import os
import argparse
from time import time


parser = argparse.ArgumentParser(prog='intersect_breaks.py', formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-f', '--file', help='path for the filtered bed file', type=str, required=True)
parser.add_argument('-a', '--AsiSI', help='path for the AsiSI bed file', type=str, required=True)
parser.add_argument('-o', '--output', help='output path for the intersected bed file', type=str, required=True)
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


def upload_bed_files(filtered_read_file, AsiSI_file):
    """
     upload files into dataframes
     :param filtered_read_file, AsiSI_file: the path for the files
     :returns  dataframes of the filtered_breaks_read and AsiSI_site
      """
    filtered_read_df = pd.read_csv(filtered_read_file, sep='\t', header=None)
    bed_AsiSI_df = pd.read_csv(AsiSI_file, sep='\t', header=None)
    return  filtered_read_df, bed_AsiSI_df

def intersect_df (bed_read_df, bed_AsiSI_df):
    """
       intersect the filtered breaks with the AsiSI_sites
       :param filtered_read_file, AsiSI_file: dataframes of the filtered_breaks_read and AsiSI_site
       :returns  the intersected breaks that founds in both dataframes
        """
    AsiSI_breaks_list = [
        site for index1, site in bed_read_df.iterrows()
        for index2, row in bed_AsiSI_df.iterrows()
        if site[2] >= row[1] and site[2] <= row[2]
    ]

    AsiSI_breaks_df = pd.DataFrame(AsiSI_breaks_list)
    outdir = create_outdir(args.output)
    AsiSI_breaks_df.to_csv(f"{outdir}/{os.path.basename(args.file).strip('filtered.bed')}.intersected.bed", sep='\t', index=False,
                           header=False)


@timer
def reads_intersecting_process():
    """
         The Main Function
          """
    breaks_df = upload_bed_files(args.file, args.AsiSI)
    AsiSI_breaks_df = intersect_df(breaks_df[0], breaks_df[1])

#####################################################

#                 MAIN                               #

#####################################################

if __name__ == '__main__':
    reads_intersecting_process()
