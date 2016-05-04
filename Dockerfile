FROM python:3.5-alpine

RUN pip install aiohttp

EXPOSE 8080

ENTRYPOINT python app.py