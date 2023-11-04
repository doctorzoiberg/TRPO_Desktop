FROM python:3.9-bullseye

ADD ./requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt
RUN pip install pytest pytest-cov

WORKDIR /home
