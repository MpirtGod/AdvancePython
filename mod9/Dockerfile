FROM python:3.8-slim-buster

RUN mkdir /app

EXPOSE 5000

COPY . /app/

RUN python -m pip install -r app/requirements.txt

WORKDIR /app

ENTRYPOINT ["python", "app.py", "-h 192.168.0.102"]