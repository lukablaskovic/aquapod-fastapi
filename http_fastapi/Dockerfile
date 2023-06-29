FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./units.csv /code/units.csv

COPY ./wait-for-postgres.sh /wait-for-postgres.sh

RUN chmod +x /wait-for-postgres.sh

RUN apt-get update && apt-get install -y postgresql-client

CMD ["/wait-for-postgres.sh", "db", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
