#!/usr/bin/env python
# coding: utf-8

import os
import sys
import runipy
from os import environ
from subprocess import call
from IPython import embed


# ### Main
# if __name__ == '__main__':
# 	path_chicago_collision_data	= '/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/Chicago_bird_collision_data/chicago_collision_data.json'
# 	path_flight_call = '/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/Chicago_bird_collision_data/flight_call.json'
# 	path_light_levels = '/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/Chicago_bird_collision_data/light_levels.json'
def main(path_chicago_collision_data, path_flight_call, path_light_levels):
	"""Get doc object of pdf, formed by combining all the given pages

	Args:
	    doc (document): Document object
	    page_numbers (list): List of pages of the PDF which are to be merged
	    dump_name (string): Name of file to be saved

	Returns:
	    doc: Doc object of the merged pdf
	"""
	html_files_address = '/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media/HTML_files/'

	# chicago_collision_data
	file_chicago_collision_data = os.path.join(html_files_address, os.path.basename(path_chicago_collision_data).split('.')[0])
	environ['chicago_collision_data'] = path_chicago_collision_data
	os.system('jupyter nbconvert --ExecutePreprocessor.timeout=200 --execute --to html mysite/core/main_chicago_collision_data.ipynb --template toc2 --output '+file_chicago_collision_data+'.html')

	# flight_call
	file_flight_call = os.path.join(html_files_address, os.path.basename(path_flight_call).split('.')[0])
	environ['flight_call'] = path_flight_call
	os.system('jupyter nbconvert --ExecutePreprocessor.timeout=200 --execute --to html mysite/core/main_flight_call.ipynb --template toc2 --output '+file_flight_call+'.html')

	# light_levels
	file_light_levels = os.path.join(html_files_address, os.path.basename(path_light_levels).split('.')[0])
	environ['light_levels'] = path_light_levels
	os.system('jupyter nbconvert --ExecutePreprocessor.timeout=200 --execute --to html mysite/core/main_light_levels.ipynb --template toc2 --output '+file_light_levels+'.html')

	# merged_Data
	environ['merged_data'] = path_chicago_collision_data +'|'+ path_flight_call +'|'+ path_light_levels
	os.system('jupyter nbconvert --ExecutePreprocessor.timeout=400 --execute --to html mysite/core/main_merged_data.ipynb --template toc2 --output '+file_chicago_collision_data+'_merged.html')
