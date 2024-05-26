# Base image for Python application
FROM python:3.9-slim

# Create a working directory within the container
WORKDIR /app

# Copy project files from host machine
COPY src/ .
# Install dependencies
RUN pip install -r requirements.txt  

# Expose port for the API service (adjust if needed)
EXPOSE 8080

# Command to run the API service
CMD ["python", "qr_code_generator.py"]

