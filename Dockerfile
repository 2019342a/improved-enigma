FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements /code/requirements
RUN pip install -r requirements/local.txt
COPY . /code/
