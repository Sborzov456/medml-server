FROM python:3.9
WORKDIR /usr/src/bid/server

RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install python3-openslide openslide-tools -y
COPY ./config/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

ENV PYTHONUNBUFFERED=1
COPY ./server .
COPY ./entrypoint.sh .
# CMD "python3 "
RUN chmod 777 entrypoint.sh
ENTRYPOINT './entrypoint.sh'