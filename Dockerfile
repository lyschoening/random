FROM python:3.5-alpine

RUN pip install aiohttp

ADD app.py .

ENTRYPOINT python app.py

EXPOSE 8080