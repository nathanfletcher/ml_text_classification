# Use Python38
FROM python:3.8-slim-buster

WORKDIR /app
# Copy requirements.txt to the docker image and install packages
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
# Set the WORKDIR to be the folder
COPY ./src/implementation /app
# Expose port 8080
EXPOSE 8080
ENV PORT 8080

# Use gunicorn as the entrypoint
CMD exec gunicorn --bind :$PORT flasksample:app --workers 1 --threads 1 --timeout 60