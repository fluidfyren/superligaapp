#import os
import pickle as pkl
import pandas as pd

def get_file_list(path):
    return ['AaB', 'AC Horsens', 'AGF', 'Brøndby IF', 'F.C. København',
            'FC Midtjylland', 'FC Nordsjælland', 'Lyngby BK',
            'OB', 'Randers FC', 'SønderjyskE', 'Vejle Boldklub']

#def get_file_list(path):       # 1.Get file names from directory
#    file_list = os.listdir(path)
#    file_list = [x[:-4] for x in file_list]
#    return file_list

def read_file(path):
    f = open(path, 'rb')
    df = pkl.load(f)
    f.close()
    return df