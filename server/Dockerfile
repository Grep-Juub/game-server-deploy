FROM python:3.10.4-slim-buster

RUN mkdir /app

WORKDIR app

ENV LISTEN_PORT 7778
ENV LISTEN_ADDRESS 127.0.0.1
ENV SERVER_TIMEOUT 600
ENV BUFFER_SIZE 1024

EXPOSE 7778/udp

RUN apt update && apt install -y lsof && rm -rf /var/lib/apt/lists/*

ADD main.py .
ADD probe.sh /usr/bin/local/probecheck

RUN chmod +x /usr/bin/local/probecheck
