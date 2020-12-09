# -*- coding: utf-8 -*-

import pandas as pd
import os
from os import listdir
from os.path import isfile, join
# from IPython import embed


# ### Reading the data 
# - Default in pandas.read_json for 'type' is 'frame' and 'orient' is 'columns'  
# - But, I have mentioned it anyways


def data_loading(path):
    """Get doc object of pdf, formed by combining all the given pages

    Args:
        doc (document): Document object
        page_numbers (list): List of pages of the PDF which are to be merged
        dump_name (string): Name of file to be saved

    Returns:
        doc: Doc object of the merged pdf
    """
    # Need to check if the file in the path actually exist

    # # making sure if the required files are present in the input path
    # file_names = [f for f in listdir(path) if isfile(join(path, f))]
    # if all([i in file_names for i in  ['chicago_collision_data.json', 'flight_call.json', 'light_levels.json']]):
    #     pass
    # else:
    #     return "Required files not present in the provided path"

    # reading the data to datafames from json format
    dataframe = pd.read_json(path, orient='columns').sort_index(axis = 0)
    
    return dataframe

def dataframe_columns_check(dataframe, required_columns):
    """Get doc object of pdf, formed by combining all the given pages

    Args:
        doc (document): Document object
        page_numbers (list): List of pages of the PDF which are to be merged
        dump_name (string): Name of file to be saved

    Returns:
        doc: Doc object of the merged pdf
    """
    # checking if the contents of the 2 lists are the same
    if set(list(dataframe.columns)) == set(required_columns):
        return True
    return False

