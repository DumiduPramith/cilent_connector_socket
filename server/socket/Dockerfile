FROM python:3-slim

COPY . /server

WORKDIR /server

ENV SOCKET_PORT=5050 IS_DOCKER=True

EXPOSE $SOCKET_PORT

CMD [ "python", "server.py" ]