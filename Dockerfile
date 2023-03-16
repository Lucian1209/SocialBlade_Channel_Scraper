# Base image
FROM python:3.9-slim-buster

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Copy the project code into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint for the container
ENTRYPOINT ["python", "main.py"]