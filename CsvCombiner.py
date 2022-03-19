import pandas as pd
import os.path
from os import path
import sys


class CsvCombiner:
    def __init__(self, inputs=None):
        if inputs is None:
            self.inputs = []
        else:
            self.inputs = inputs[1:]

    #Checking for correct inputs
    def check_input(self):
        if len(self.inputs) < 1:
            return False
        else:
            return True

    #Checking if files exist in the proper directory
    def check_directory(self):
        for i in self.inputs:
            if not path.exists(i):
                return (False, i)
        return (True, None)

    #Combining CSV files
    def csv_combiner(self):
        for i, files in enumerate(self.inputs):
            if i == 0:
                print('email_hash,category,filename')
            name = files.split('/')[-1]

    #Using blocks to reduce memory usage and read csv files according to given chunk size
            for blocks in pd.read_csv(files, chunksize=100000):
                blocks[name] = name
                print(blocks.to_csv(header=False, index=False,
                                    chunksize=100000), end='')

    #Executing all the above methods to get output 
    def executecsvcombiner(self):
        if self.check_input():
            directory_rg = self.check_directory()

            if directory_rg[0]:
                self.csv_combiner()
            else:
                print('File: ' + directory_rg[1] + ' not found.', end='')
        else:
            print('Please input correct inputs.', end='')


#main function
def main():
    CSVFilesCombine = CsvCombiner(sys.argv)
    CSVFilesCombine.executecsvcombiner()


if __name__ == "__main__":
    main()
