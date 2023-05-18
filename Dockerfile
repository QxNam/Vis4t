FROM python:3.11.1-slim

WORKDIR /Vis4T_main

COPY . .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 
RUN cat requirements.txt | xargs -n 1 pip install

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]