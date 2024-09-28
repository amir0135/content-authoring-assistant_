# Start from a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install curl and other dependencies
RUN apt-get update && apt-get install -y curl

# Copy requirements.txt and install dependencies
# Updated path for requirements.txt (now in config/)
COPY config/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
# Updated paths for src and infra directories
COPY src/ ./src/
COPY infra/ ./infra/

# Expose the port and run the FastAPI app
EXPOSE 8000

# Updated CMD to match the new path of main.py in src/
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]