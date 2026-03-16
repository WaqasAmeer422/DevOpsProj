FROM python:3.9-slim

WORKDIR /app

# Install flask
RUN pip install flask

COPY hello.py .

# Open port 5000 to the world
EXPOSE 5000

CMD ["python", "hello.py"]