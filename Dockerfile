# Step 1: Use a small Python image
FROM python:3.9-slim

# Step 2: Set the folder inside the container
WORKDIR /app

# Step 3: Copy your script into the container
COPY hello.py .

# Step 4: Run the script
CMD ["python", "hello.py"]