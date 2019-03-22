FROM python:3.6
MAINTAINER myadav@hub9.io


COPY ./first_app /first_app

WORKDIR /first_app

RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
