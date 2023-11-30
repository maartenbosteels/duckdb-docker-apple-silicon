    # FROM ubuntu:22.04

# ARG DEBCONF_NOWARNINGS="yes"
# ARG DEBIAN_FRONTEND="noninteractive"
# RUN apt-get -yqq update && apt-get install -yqq --no-install-recommends apt-utils

# # https://bobcares.com/blog/debian_frontendnoninteractive-docker/
# ARG DEBIAN_FRONTEND=noninteractive
# RUN apt-get -y install python3.10 python3.10-venv

# RUN apt-get -y install install gcc gcc-c++ git 

FROM public.ecr.aws/lambda/python:3.11

RUN pip3 install --upgrade pip \
    && yum install gcc gcc-c++ git -y


WORKDIR /app

RUN python -m venv .venv

RUN . .venv/bin/activate 

RUN . .venv/bin/activate  && pip install duckdb --no-binary duckdb

ADD main.py /app/

ENTRYPOINT ["/app/.venv/bin/python3", "-u" , "./main.py"]