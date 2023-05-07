FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-devel
WORKDIR /usr/src/web/nnapi

RUN python -m pip install --upgrade pip
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./r2.txt .
RUN pip install -r ./r2.txt
ARG MEDIA_ROOT=/usr/src/web/media
ENV MEDIA_ROOT=$MEDIA_ROOT
RUN mkdir $MEDIA_ROOT
ENV PYTHONUNBUFFERED=1
CMD uvicorn --host ${NN_API_HOST} --port ${NN_API_PORT} --workers 1 --reload server.main:app 