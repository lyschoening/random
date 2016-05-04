FROM python:3.5-alpine

RUN pip install aiohttp

EXPOSE 5000

ENTRYPOINT python app.py
