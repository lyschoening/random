FROM python:3.5-alpine

RUN pip install aiohttp

ADD app.py .

EXPOSE 8080

ENTRYPOINT python app.py
