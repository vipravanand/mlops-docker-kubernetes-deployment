FROM python:3.10-slim
RUN apt-get update && apt-get install -y vim

WORKDIR /app

COPY /requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . ./

# Run the flask service on container startup
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 AEgunicorn:app