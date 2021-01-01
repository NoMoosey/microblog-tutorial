FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y python3.8 python3-venv python3-dev

RUN groupadd -r microblog && useradd -r -g microblog microblog

WORKDIR /home/microblog

COPY requirements.txt requirements.txt
RUN python3.8 -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY docker docker
COPY microblog.py config.py ./
RUN chmod a+x ./docker/boot.sh

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["bash", "./docker/boot.sh"]