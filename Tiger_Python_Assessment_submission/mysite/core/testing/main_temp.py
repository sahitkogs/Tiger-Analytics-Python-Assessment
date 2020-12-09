#!/usr/bin/env python
# coding: utf-8

# ### Required packages  

import logging
import pandas as pd
import os
from os import listdir
from os.path import isfile, join
# from IPython import embed

from data_loading import data_loading
from data_cleaning import column_renaming, removing_duplicates, removing_missing_values
from data_merging import data_merging
from helpers import data_summary

# LOGGER = logging.getLogger('prospectus_extraction')
# if not LOGGER.handlers:
#     LOGGER.setLevel(logging.DEBUG)
#     CH = logging.StreamHandler()
#     CH.setLevel(logging.DEBUG)
#     CH.setFormatter(logging.Formatter(
#         '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s'
#     ))
#     LOGGER.addHandler(CH)



# ### Main
if __name__ == '__main__':

    rawdata_path = 'C:/Users/SAHIT/Documents/MLE_opportunities_with_Tiger_Analytics/Chicago_bird_collision_data/'

    # Data Loading
    flight_call, chicago_collision_data, light_levels = data_loading(rawdata_path)
    flight_call.to_csv('data_loading_flight_call.csv', index=False)
    chicago_collision_data.to_csv('data_loading_chicago_collision_data.csv', index=False)
    light_levels.to_csv('data_loading_light_levels.csv', index=False)

    # Data Cleaning
    flight_call, light_levels, chicago_collision_data = column_renaming(flight_call, light_levels, chicago_collision_data)
    flight_call.to_csv('column_renaming_flight_call.csv', index=False)
    chicago_collision_data.to_csv('column_renaming_chicago_collision_data.csv', index=False)
    light_levels.to_csv('column_renaming_light_levels.csv', index=False)

    flight_call, light_levels, chicago_collision_data = removing_duplicates(flight_call, light_levels, chicago_collision_data)
    flight_call.to_csv('removing_duplicates_flight_call.csv', index=False)
    chicago_collision_data.to_csv('removing_duplicates_chicago_collision_data.csv', index=False)
    light_levels.to_csv('removing_duplicates_light_levels.csv', index=False)

    flight_call, light_levels, chicago_collision_data = removing_missing_values(flight_call, light_levels, chicago_collision_data)
    flight_call.to_csv('removing_missing_values_flight_call.csv', index=False)
    chicago_collision_data.to_csv('removing_missing_values_chicago_collision_data.csv', index=False)
    light_levels.to_csv('removing_missing_values_light_levels.csv', index=False)

    # summary of the raw dataframes
    for dataframe in (flight_call, light_levels, chicago_collision_data):
        data_summary(dataframe)
        
    # merging the raw data
    clean_birds_lightScore = data_merging(flight_call, light_levels, chicago_collision_data)
    clean_birds_lightScore.to_csv('data_merging_clean_birds_lightScore.csv', index=False)
    
    data_summary(clean_birds_lightScore)

