# FROM python:3.9-slim

# # Arbeitsverzeichnis erstellen
# WORKDIR /app

# # Systemabhängigkeiten installieren
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     wget \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# RUN apt-get update && apt-get install -y \
#     git \
#     python3-dev \
#     build-essential \
#     libopenblas-dev \
#     libssl-dev \
#     libcurl4-openssl-dev \
#     cmake \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 8000

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# RUN apt-get update -y && apt-get install -y \
#     python3.10 \
#     python3.10-dev \
#     python3-pip \
#     build-essential \
#     wget \
#     curl \
#     git \
#     python3-dev \
#     build-essential \
#     libopenblas-dev \
#     libssl-dev \
#     libcurl4-openssl-dev \
#     cmake \
#     && rm -rf /var/lib/apt/lists/*
FROM python:3.10-slim
ENV DEBIAN_FRONTEND=noninteractive
ENV CUDA_HOME=/usr/local/cuda
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    python3-dev \
    libopenblas-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . .
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
#RUN pip install packaging
RUN pip install numpy==1.21.2
RUN pip install torch==2.1.2
RUN pip install -r requirements.txt
#RUN pip install git+https://github.com/HazyResearch/flash-attention.git
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]




# Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed dependencies specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 8080 available to the world outside this container
# EXPOSE 8080

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]