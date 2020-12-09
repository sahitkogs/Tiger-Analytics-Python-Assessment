#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import unittest

# Bring your packages onto the path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from data_loading import data_loading
from data_cleaning import column_renaming, removing_duplicates, removing_missing_values
from data_merging import data_merging
from helpers import data_summary

"""#################################################
## TO DO ##
1. Need to structure the class better using the __init__
2. Build tests on the data type of the outputs
3. Build tests on the levele of the tables in the input and the output


#################################################"""

rawdata_path = 'C:/Users/SAHIT/Documents/MLE_opportunities_with_Tiger_Analytics/Chicago_bird_collision_data/'

class Test_processing(unittest.TestCase):

	def test_data_loading(self):
		"""validating the output of the data_loading function

		Args:

		Returns:
		    asserts if the three outputs have the same lenghts and values for all the columns in the output
		"""
		flight_call, chicago_collision_data, light_levels = data_loading(rawdata_path)

		# checking if the columns of the datframe are the same
		# self.assertListEqual(list(data_loading_flight_call.columns), list(flight_call.columns))
		self.assertListEqual(list(data_loading_chicago_collision_data.columns), list(chicago_collision_data.columns))
		self.assertListEqual(list(data_loading_light_levels.columns), list(light_levels.columns))

		# checking if the count of the columns of the datframe are the same
		self.assertCountEqual(list(data_loading_chicago_collision_data.columns), list(chicago_collision_data.columns))
		self.assertCountEqual(list(data_loading_light_levels.columns), list(light_levels.columns))

	def test_column_renaming(self):
		"""validating the output of the column_renaming function

		Args:

		Returns:
		    asserts if the three outputs have the same lenghts and values for all the columns in the output
		"""

		flight_call, chicago_collision_data, light_levels = column_renaming(data_loading_flight_call, data_loading_chicago_collision_data, data_loading_light_levels)

		# checking if the columns of the datframe are the same
		self.assertListEqual(list(column_renaming_flight_call.columns), list(flight_call.columns))
		self.assertListEqual(list(column_renaming_chicago_collision_data.columns), list(chicago_collision_data.columns))
		self.assertListEqual(list(column_renaming_light_levels.columns), list(light_levels.columns))

		# checking if the count of the  columns of the datframe are the same
		self.assertCountEqual(list(column_renaming_flight_call.columns), list(flight_call.columns))
		self.assertCountEqual(list(column_renaming_chicago_collision_data.columns), list(chicago_collision_data.columns))
		self.assertCountEqual(list(column_renaming_light_levels.columns), list(light_levels.columns))

	def test_removing_duplicates(self):
		"""validating the output of the removing the duplicates of the input dataframes

		Args:

		Returns:
		    asserts if the three outputs have the same lenghts and values for all the columns in the output
		"""

		flight_call, chicago_collision_data, light_levels = removing_duplicates(removing_missing_values_flight_call, removing_missing_values_chicago_collision_data, removing_missing_values_light_levels)

		# checking if the columns of the datframe are the same
		self.assertListEqual(list(removing_duplicates_flight_call.columns), list(flight_call.columns))
		self.assertListEqual(list(removing_duplicates_chicago_collision_data.columns), list(chicago_collision_data.columns))
		self.assertListEqual(list(removing_duplicates_light_levels.columns), list(light_levels.columns))

		# checking if the count of the columns of the datframe are the same
		self.assertCountEqual(list(removing_duplicates_flight_call.columns), list(flight_call.columns))
		self.assertCountEqual(list(removing_duplicates_chicago_collision_data.columns), list(chicago_collision_data.columns))
		self.assertCountEqual(list(removing_duplicates_light_levels.columns), list(light_levels.columns))

	def test_removing_missing_values(self):
		"""validating the output of the removing rows of the missing values in the dataframe inputs

		Args:

		Returns:
		    asserts if the three outputs have the same lenghts and values for all the columns in the output
		"""

		flight_call, chicago_collision_data, light_levels = removing_missing_values(column_renaming_flight_call, column_renaming_chicago_collision_data, column_renaming_light_levels)

		# checking if the columns of the datframe are the same
		self.assertListEqual(list(removing_missing_values_flight_call.columns), list(flight_call.columns))
		self.assertListEqual(list(removing_missing_values_chicago_collision_data.columns), list(chicago_collision_data.columns))
		self.assertListEqual(list(removing_missing_values_light_levels.columns), list(light_levels.columns))

		# checking if the count of the columns of the datframe are the same
		self.assertCountEqual(list(removing_missing_values_flight_call.columns), list(flight_call.columns))
		self.assertCountEqual(list(removing_missing_values_chicago_collision_data.columns), list(chicago_collision_data.columns))
		self.assertCountEqual(list(removing_missing_values_light_levels.columns), list(light_levels.columns))

	# def test_data_merging(self):
		"""Get doc object of pdf, formed by combining all the given pages

		Args:
		    doc (document): Document object
		    page_numbers (list): List of pages of the PDF which are to be merged
		    dump_name (string): Name of file to be saved

		Returns:
		    doc: Doc object of the merged pdf
		"""

	# 	clean_birds_lightScore = data_merging(removing_missing_values_flight_call, removing_missing_values_chicago_collision_data, removing_missing_values_light_levels)

	# 	# checking if the columns of the datframe are the same
	# 	self.assertListEqual(list(clean_birds_lightScore.columns), list(data_merging_clean_birds_lightScore.columns))



if __name__ == '__main__':

	# Reading the CSVs generated from the standard run and they are compared to the intermidiatte steps in the respective unit tests

	# Outputs of Data Loading
	data_loading_flight_call = pd.read_csv('data_loading_flight_call.csv')
	data_loading_chicago_collision_data = pd.read_csv('data_loading_chicago_collision_data.csv')
	data_loading_light_levels = pd.read_csv('data_loading_light_levels.csv')

	# Outputs of Column Renaming
	column_renaming_flight_call = pd.read_csv('column_renaming_flight_call.csv')
	column_renaming_chicago_collision_data = pd.read_csv('column_renaming_chicago_collision_data.csv')
	column_renaming_light_levels = pd.read_csv('column_renaming_light_levels.csv')

	# Outputs of Removing the missing values
	removing_missing_values_flight_call = pd.read_csv('removing_missing_values_flight_call.csv')
	removing_missing_values_chicago_collision_data = pd.read_csv('removing_missing_values_chicago_collision_data.csv')
	removing_missing_values_light_levels = pd.read_csv('removing_missing_values_light_levels.csv')

	# Outputs of Removing Duplicates
	removing_duplicates_flight_call = pd.read_csv('removing_duplicates_flight_call.csv')
	removing_duplicates_chicago_collision_data = pd.read_csv('removing_duplicates_chicago_collision_data.csv')
	removing_duplicates_light_levels = pd.read_csv('removing_duplicates_light_levels.csv')

	data_merging_clean_birds_lightScore = pd.read_csv('data_merging_clean_birds_lightScore.csv')

	unittest.main()