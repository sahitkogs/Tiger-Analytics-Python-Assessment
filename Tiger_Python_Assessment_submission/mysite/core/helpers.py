# -*- coding: utf-8 -*-

import pandas as pd

# ### Utility functions 
# #### Data summary 


def data_summary(dataframe):
    """Get doc object of pdf, formed by combining all the given pages

    Args:
        doc (document): Document object
        page_numbers (list): List of pages of the PDF which are to be merged
        dump_name (string): Name of file to be saved

    Returns:
        doc: Doc object of the merged pdf
    """
    print("Dataframe name  :", dataframe.name)
    print ("\nRows     : " ,dataframe.shape[0])
    print ("Columns  : " ,dataframe.shape[1])
    print ("\nFeatures : \n" ,dataframe.columns.tolist())
    print ("\nMissing values in each column:  ", dataframe.isnull().sum().values.tolist())
    print ("\nUnique values :  \n",dataframe.nunique())
    print ("\n\n ######################################")

