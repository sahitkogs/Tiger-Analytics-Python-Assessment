# Vulnerability to Artificial Light in Nocturnal Flight-calling Birds - Report
This project analyses the observed data at McCormick Place or greater Chicago area about 
the number of deaths of migratory birds caused due to artificial light

## Team Members 

- Sahit Koganti

## Data Source

- The data is part of the analysis performed as research work by Benjamin M. Winger; Title: Nocturnal flight-calling behaviour predicts vulnerability to artificial light in migratory birds
- The research paper can be accessed at 

- Access the metadata from https://github.com/rfordatascience/tidytuesday/tree/47567cb80846739c8543d158c1f3ff226c7e5a5f/data/2019/2019-04-30#bird_collisionscsv

- Raw data required for this project are:
	- chicago_collision_data.json
	- flight_call.json
	- light_levels.json

## Objective

- The client who uses the web-based front end, has a need to continuously generate reports based on the inputed raw data. 
- Once inputed in the frontend, the reports keeps populating in the dashboard portal at the interval set in the Airflow Scheduler. The Airflow task details can be accessed at Airflow web UI aswell.
- Whenever the user recieves new raw data inupts, it needs to be uploaded in the frontend and platform automatically picksup the new data for further generated reports
- An email trigger has been setup for sending every generated report through Airflow 

## Technologies used:

- Django
- HTML/CSS based frontend
- AWS LightSail
- Docker
- Airflow
- Jupyter notebooks
- Python 3.7
- SQLite database

## Code structure

Backend Code Structure
    1. main_airflow.py 
       (Defines the DAG; Creates PythonOperator tasks; Triggers the task workflow)
        A) task_chicago_collision_data
           (Triggers main_chicago_collision_data.ipynb file)
            a) data_loading.py, data_cleaning.py, Other EDA functions
               (We will be using functions from the above .py files for all the data processing and report generation steps)
        B) task_flight_call
           (Triggers main_chicago_collision_data.ipynb file)
            a) data_loading.py, data_cleaning.py, Other EDA functions
               (We will be using functions from the above .py files for all the data processing and report generation steps)
        C) task_light_levels
           (Triggers main_chicago_collision_data.ipynb file)
            a) data_loading.py, data_cleaning.py, Other EDA functions
               (We will be using functions from the above .py files for all the data processing and report generation steps)

## Testing

- I have built few basic unit tests for some of the functions in the backend

## Deployment Procedure

cd /Tiger_Python_Assessment_submission/

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

## Pending tasks

- Integration of Airflow scheduler into the workflow for generating the reports
- Creating logs for the coding module
- MOre unit tests for the functions used
- Building a classification model for better understanding how each of the features influence the death of the birds.