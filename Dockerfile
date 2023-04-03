# Use a Python 3 base image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script that contains your FastAPI app to the working directory
COPY main.py .

# Expose port 80 for incoming HTTP requests
EXPOSE 80

# Set the default command to run the FastAPI app using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]