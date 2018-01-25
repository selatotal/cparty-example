FROM ubuntu:latest
MAINTAINER Tales Viegas "tales.viegas@ilegra.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV CPARTY_SETTINGS "config/cparty.config"
ENTRYPOINT ["python"]
CMD ["cparty.py"]
