import airflow
from airflow.models import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.email_operator import EmailOperator
# from dags.process import process_data
from datetime import datetime, timedelta

# Update the default arguments and apply them to the DAG.
default_args = {
				'owner': 'sahitkogs',
				'start_date': airflow.utils.dates.days_ago(2),
				'email': ['airflow@example.com'],
				'email_on_failure': False,
				'email_on_retry': False,
				}

dag = DAG(dag_id='chicago_birds_collision', 
			default_args=default_args,
			description='Vulnerability to artificial light in migratory birds - Report')


def run_chicago_collision_data(*op_args):
	"""Get doc object of pdf, formed by combining all the given pages

	Args:
	    doc (document): Document object
	    page_numbers (list): List of pages of the PDF which are to be merged
	    dump_name (string): Name of file to be saved

	Returns:
	    doc: Doc object of the merged pdf
	"""
	path_chicago_collision_data = op_args[0]

	html_files_address = '/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media/HTML_files/'

	# chicago_collision_data
	file_chicago_collision_data = os.path.join(html_files_address, os.path.basename(path_chicago_collision_data).split('.')[0])
	environ['chicago_collision_data'] = path_chicago_collision_data
	os.system('jupyter nbconvert --ExecutePreprocessor.timeout=200 --execute --to html mysite/core/main_chicago_collision_data.ipynb --no-input --output '+file_chicago_collision_data+'.html')


def run_flight_call(*op_args):
	"""Get doc object of pdf, formed by combining all the given pages

	Args:
	    doc (document): Document object
	    page_numbers (list): List of pages of the PDF which are to be merged
	    dump_name (string): Name of file to be saved

	Returns:
	    doc: Doc object of the merged pdf
	"""
	path_flight_call = op_args[0]
	html_files_address = '/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media/HTML_files/'

	# flight_call
	file_flight_call = os.path.join(html_files_address, os.path.basename(path_flight_call).split('.')[0])
	environ['flight_call'] = path_flight_call
	os.system('jupyter nbconvert --ExecutePreprocessor.timeout=200 --execute --to html mysite/core/main_flight_call.ipynb --no-input --output '+file_flight_call+'.html')


def run_light_levels(*op_args):
	"""Get doc object of pdf, formed by combining all the given pages

	Args:
	    doc (document): Document object
	    page_numbers (list): List of pages of the PDF which are to be merged
	    dump_name (string): Name of file to be saved

	Returns:
	    doc: Doc object of the merged pdf
	"""
	path_light_levels = op_args[0]
	html_files_address = '/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media/HTML_files/'

	# light_levels
	file_light_levels = os.path.join(html_files_address, os.path.basename(path_light_levels).split('.')[0])
	environ['light_levels'] = path_light_levels
	os.system('jupyter nbconvert --ExecutePreprocessor.timeout=200 --execute --to html mysite/core/main_light_levels.ipynb --no-input --output '+file_light_levels+'.html')


def run_chicago_collision_data_merged(*op_args):
	"""Get doc object of pdf, formed by combining all the given pages

	Args:
	    doc (document): Document object
	    page_numbers (list): List of pages of the PDF which are to be merged
	    dump_name (string): Name of file to be saved

	Returns:
	    doc: Doc object of the merged pdf
	"""
	path_chicago_collision_data, path_flight_call, path_light_levels = [op_args[0], op_args[1], op_args[2]]
	html_files_address = '/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media/HTML_files/'

	# merged_Data
	environ['merged_data'] = path_chicago_collision_data +'|'+ path_flight_call +'|'+ path_light_levels
	os.system('jupyter nbconvert --ExecutePreprocessor.timeout=400 --execute --to html mysite/core/main_merged_data.ipynb --no-input --output '+file_chicago_collision_data+'_merged.html')


if __name__ == '__main__':
	path_chicago_collision_data, path_flight_call, path_light_levels = [sys.argv[0], sys.argv[1], sys.argv[2]]

	task_chicago_collision_data = PythonOperator(task_id='chicago_collision_data', 
	                             python_callable=run_chicago_collision_data,
	                             provide_context=True,
	                             op_args=[path_chicago_collision_data],
	                             dag=dag)

	task_flight_call = PythonOperator(task_id='flight_call', 
	                             python_callable=run_flight_call,
	                             provide_context=True,
	                             op_args=[path_flight_call],
	                             dag=dag)

	task_light_levels = PythonOperator(task_id='light_levels', 
	                             python_callable=run_light_levels,
	                             provide_context=True,
	                             op_args=[path_light_levels],
	                             dag=dag)

	task_chicago_collision_data_merged = PythonOperator(task_id='chicago_collision_data_merged', 
	                             python_callable=run_chicago_collision_data_merged,
	                             provide_context=True,
	                             op_args=[path_chicago_collision_data, path_flight_call, path_light_levels],
	                             dag=dag)

	[task_chicago_collision_data, task_flight_call, task_light_levels] >> task_chicago_collision_data_merged

