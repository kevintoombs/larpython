#download zip from https://goo.gl/SV22tg

from os import listdir
import pandas as pd

def simple_function(in_string):
    '''
    This is called a doc string
    '''
    print(in_string)
    
def math_function(x,y,op):
    if (op == "add"):
        z = x + y
        return z
    if(op == "multiply"):
        return x * y
    print("Error: Operation not supported")
    
def get_csv_filenames(path):
    list_of_files = listdir(path)
    csv_filenames = []
    
    for filename in list_of_files:
        if (filename.endswith(".csv") or filename.endswith(".CSV")):
            csv_filenames.append(filename)
            
    return csv_filenames

def get_csv_pathnames(path):
    filenames = get_csv_filenames(path)
    filepaths = []
    for name in filenames:
        filepaths.append(path + name)
    return filepaths

def create_dataframe_from_csv(csv, header=0):
    frame = pd.read_csv(csv, header=header)
    return frame

def create_dataframe_from_csv_list(list_of_csvs, header=0):
    list_of_frames = []
    for csv in list_of_csvs:
        frame = create_dataframe_from_csv(csv, header)
        list_of_frames.append(frame)
    big_frame = pd.concat(list_of_frames)
    big_frame.index = range(len(big_frame)) #fixes indexes
    return big_frame

def create_dataframe_from_dir(dirpath, header=0):
    '''
    This function takes a dir ('./folder/') and returns a pandas dataframe
    Inputs: dirpath (folder you want data from), header optional (row header is found on)
    Output: pandas dataframe
    '''
    paths = get_csv_pathnames(dirpath)
    frame = create_dataframe_from_csv_list(paths,header)
    return frame

if __name__ == "__main__":
    simple_function("hello")
    simple_function("hi")
    #print(math_function(2,4,"add"))
    sum_of = math_function(2,4,"add")
    product_of = math_function(2,4,"multiply")
    print(sum_of, product_of)
    
    
    csvs = get_csv_pathnames('./')
    #print(csvs)
    csvs2 = get_csv_pathnames('./afolder/')
    
    frame = create_dataframe_from_csv_list((csvs+csvs2))
    print(frame)
    
    afolder_frame = create_dataframe_from_dir('./afolder/')
    print(afolder_frame)
    






