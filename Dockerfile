# FROM ubuntu:23.04
FROM alpine

ENV food=bar
ENV name=amitsk
# USER ammm:maaa

WORKDIR /app
COPY . /app

RUN apk update && apk upgrade --available 
RUN apk add --update python3


CMD ["python3" "./app.py" ]
