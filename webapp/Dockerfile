# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Define environment variable to make Python print messages immediately
ENV PYTHONUNBUFFERED=1
RUN python keys_generator.py

# Run the application
CMD ["python", "app.py"]
