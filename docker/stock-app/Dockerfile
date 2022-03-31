FROM python:3.8.0
# Python docker images: https://github.com/docker-library/docs/tree/master/python/

# Copy the src
WORKDIR /app
COPY src/ /app/src/
COPY ./requirements.txt /app

# Install python dependencies
RUN apt update
RUN apt install libpq-dev python3-dev -y
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r /app/requirements.txt

ENTRYPOINT ["python3", "/app/src/run.py"]

