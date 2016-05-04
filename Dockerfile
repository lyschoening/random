FROM python:3.5

RUN pip install aiohttp aiozmq msgpack-python

ADD app.py .

ENTRYPOINT python ./app.py

EXPOSE 8080