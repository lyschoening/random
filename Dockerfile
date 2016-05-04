FROM python:3.5-alpine

RUN pip install aiohttp

ADD . app.py

EXPOSE 5000

ENTRYPOINT python app.py
