FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11


# Creating the root directory of the project
RUN mkdir /data_service

# Set the working directory
WORKDIR /data_service

# copy project
COPY . /data_service/

# Set python NOT to write *.pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Set python output straight to the terminal
ENV PYTHONBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get -y install vim

ARG SECRET_ENVS
COPY $SECRET_ENVS .env
