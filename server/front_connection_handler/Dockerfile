FROM python:3-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENV SOCKET_PORT=5050 IS_DOCKER=True WEBSOCKET_PORT=80

EXPOSE $SOCKET_PORT $WEBSOCKET_PORT

CMD [ "gunicorn","--bind", "0.0.0.0:8000", "-k", "eventlet", "socket_io_server:app" ]