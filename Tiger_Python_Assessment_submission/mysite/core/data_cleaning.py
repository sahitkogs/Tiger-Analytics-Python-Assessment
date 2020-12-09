# -*- coding: utf-8 -*-

import pandas as pd

# ### Data Cleaning

# #### Renaming columns
# - Column names need to be replaced for **flight_call** dataset as prescribed in the problem statement
#     - Species -> Genus
#     - Family -> Species
#     - Collisions -> Family
#     - Call -> Flight Call


def column_renaming(dataframe, required=True):
    """Get doc object of pdf, formed by combining all the given pages

    Args:
        doc (document): Document object
        page_numbers (list): List of pages of the PDF which are to be merged
        dump_name (string): Name of file to be saved

    Returns:
        doc: Doc object of the merged pdf
    """
    if required == True:
        dataframe.rename(columns={'Species': 'Genus', 'Family': 'Species', 'Collisions': 'Family', 'Call': 'Flight Call'}, inplace=True)
    else:
        pass
    return dataframe


# ####  Dropping the duplcate rows
def removing_duplicates(dataframe):
    """Get doc object of pdf, formed by combining all the given pages

    Args:
        doc (document): Document object
        page_numbers (list): List of pages of the PDF which are to be merged
        dump_name (string): Name of file to be saved

    Returns:
        doc: Doc object of the merged pdf
    """
    # Checking the level of the 

    if dataframe.name == 'light_levels':
        dataframe.drop_duplicates(subset=['Date'], keep='last', inplace=True)
    else:
        dataframe.drop_duplicates(inplace=True)
    
    return dataframe


# ####  Missing values treatment


def removing_missing_values(dataframe):
    """Get doc object of pdf, formed by combining all the given pages

    Args:
        doc (document): Document object
        page_numbers (list): List of pages of the PDF which are to be merged
        dump_name (string): Name of file to be saved

    Returns:
        doc: Doc object of the merged pdf
    """

    dataframe.dropna(axis='rows', how='any', inplace=True)
    
    return dataframe