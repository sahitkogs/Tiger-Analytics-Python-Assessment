# Base Image
FROM python:3.7

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv
RUN pip3 install django-crispy-forms==1.7.2
RUN pip3 install Pillow==5.3.0
RUN pip3 install pytz==2018.4
RUN pip3 install ipython==7.18.1
RUN pip3 install runipy==0.1.5
RUN pip3 install pandas==1.1.1
RUN pip3 install nbconvert==5.6.1
RUN pip3 install numpy==1.18.5
RUN pip3 install Django==2.1.3
RUN pip3 install gunicorn==20.0.4


# Install project dependencies
# RUN pipenv install --skip-lock --system --dev

EXPOSE 8000
CMD gunicorn mysite.wsgi:application --bind 0.0.0.0:$PORT
