FROM alpine:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apk add --no-cache chromium
RUN apk add --no-cache chromium-chromedriver

# Install Python and set the version
RUN apk add --no-cache python3
RUN apk add py3-pip

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip3 install -r /app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the entrypoint when the container starts
CMD ["python", "main.py"]