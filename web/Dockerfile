# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip; pip3 install --no-cache-dir Flask gunicorn

# Make port 6000 available to the world outside this container
EXPOSE 6000

# # Run web.py when the container launches
CMD ["gunicorn","-b", "0.0.0.0:6000", "--workers=4", "--threads=8", \
"--worker-class=gthread", "--worker-tmp-dir", "/dev/shm", "web:app"]
