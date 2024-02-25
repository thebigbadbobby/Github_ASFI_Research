# Use an official python image as a parent image
FROM python:3.8-slim

# Install Flask and Pillow
RUN pip install Flask Pillow


COPY ./app /app
COPY ./images /app/images

WORKDIR /app

CMD ["python", "app.py"]
# # Copy the current directory contents into the container
# COPY . /app

# # Set the working directory
# WORKDIR /app

# # Run the Flask app
# CMD ["python", "app.py"]
