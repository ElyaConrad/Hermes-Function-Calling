FROM pytorch:1.8.0-cuda11.1-cudnn8-runtime

ENV DEBIAN_FRONTEND=noninteractive

#ENV CUDA_HOME=/usr/local/cuda

COPY . .
RUN python -m venv /opt/venv

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]