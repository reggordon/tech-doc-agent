# Use a Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies for WeasyPrint and Pango
RUN apt-get update && apt-get install -y \
    libpango1.0-dev libcairo2-dev libgdk-pixbuf2.0-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire application into the container
COPY . /app/

# Expose the port the app will run on (optional)
EXPOSE 8501

# Set the command to run your app (for example, Streamlit app)
CMD ["streamlit", "run", "ui.py"]
