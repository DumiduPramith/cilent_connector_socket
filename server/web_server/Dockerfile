FROM python:3-slim

COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver" ]