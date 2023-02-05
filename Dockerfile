# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the environment variable for Elasticsearch URL
ENV ES_URL http://127.0.0.1:9200

# Expose the default Flask port
EXPOSE 5000

# Define the command to run the application
# CMD ["flask", "run", "--host=0.0.0.0"]
# CMD ["sleep", "6000"]
