# -*- coding: utf-8 -*-

import pandas as pd

# ### Data Merging 


def data_merging(flight_call, light_levels, chicago_collision_data):
    """Get doc object of pdf, formed by combining all the given pages

    Args:
        doc (document): Document object
        page_numbers (list): List of pages of the PDF which are to be merged
        dump_name (string): Name of file to be saved

    Returns:
        doc: Doc object of the merged pdf
    """

    clean_birds = pd.merge(chicago_collision_data, flight_call,  how='left', on=["Genus", "Species"])
    clean_birds_lightScore = pd.merge(clean_birds, light_levels,  how='left', on=["Date"])
    clean_birds_lightScore.name = 'clean_birds_lightScore'
    
    return clean_birds_lightScore