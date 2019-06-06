FROM ubuntu:18.04

# Python installation
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip

# Certbot installation
RUN apt-get install -y software-properties-common
RUN add-apt-repository universe
RUN add-apt-repository ppa:certbot/certbot

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install certbot

# Setup application
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app
EXPOSE 5000

#Setup certbot
ARG cert_email=sample.test@gmail.com
RUN certbot register -m $cert_email --non-interactive --agree-tos
RUN mkdir -p /var/www/certs

ENTRYPOINT ["python3"]
CMD ["app.py"]