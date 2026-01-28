# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server code
COPY server.py .

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
# Use --host=0.0.0.0 so it's accessible outside the container
CMD ["python", "server.py"]
