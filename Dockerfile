# 1. Start with a lightweight version of Python
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy and install the required libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the application code
COPY . .

# 5. The command to run the application when the container starts
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]