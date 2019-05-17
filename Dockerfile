FROM python:3.6

#### app related steps ####
# Set working directory to app location
WORKDIR /app
# Copy in python requirements file
COPY requirements.txt /app/requirements.txt
# Install with pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code to image
COPY . /app
CMD ["python", "run.py"]
