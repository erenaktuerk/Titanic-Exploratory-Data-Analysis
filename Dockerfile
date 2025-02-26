# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8050 in case you develop an interactive dashboard later
EXPOSE 8050

# Define environment variable for unbuffered output
ENV PYTHONUNBUFFERED=1

# Run the main script
CMD ["python", "main.py"]