FROM nvidia/cuda:12.4.0-runtime-ubuntu22.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libgl1-mesa-glx \
        libglib2.0-0 \
        libsm6 \
        libxrender1 \
        libxext6 \
        python3 \
        python3-pip \
        git \
        curl \
        wget \
        && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache-dir --upgrade pip

COPY requirements.txt requirements_gpu.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_gpu.txt

COPY . .

RUN wget https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov10x.pt -P ./models/vitpose/yolo_models

EXPOSE 8000

CMD ["gunicorn", "api.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornH11Worker", "--bind", "0.0.0.0:8000"]
