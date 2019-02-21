FROM python:3.6.5
MAINTAINER hide <sharehead@gmail.com>

COPY Pipfile ./home
COPY Pipfile.lock ./home
WORKDIR /home
RUN pip install pipenv
RUN pipenv install --system
RUN apt-get update && apt-get install -y uwsgi-plugin-python3 \
    && apt-get install -y uwsgi-plugin-python && apt-get install -y vim \
    && apt-get install -y git
RUN apt-get update && apt-get install -y vim && apt-get install -y git
RUN pip install uwsgi && pip install git+https://github.com/Supervisor/supervisor
CMD ./docker/config/run-dev.sh