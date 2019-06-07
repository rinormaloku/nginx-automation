FROM python:3.6.6-alpine
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

RUN apk update -f \
  && apk --no-cache add -f \
  openssl \
  coreutils \
  bind-tools \
  curl \
  socat \
  tzdata \
  && rm -rf /var/cache/apk/*
RUN apk upgrade --no-cache 
RUN apk add bash --no-cache  

COPY . /app

ARG acmeShVersion=2.8.1
RUN mkdir -p /var/custom/scripts/
RUN wget https://github.com/Neilpang/acme.sh/archive/$acmeShVersion.zip
RUN unzip -p $acmeShVersion.zip acme.sh-$acmeShVersion/acme.sh > /var/custom/scripts/acme.sh
RUN rm -rf $acmeShVersion.zip
RUN chmod -R 700 /var/custom/scripts/acme.sh
RUN sed -i '4116i\    _sleep 10' /var/custom/scripts/acme.sh
RUN mkdir -p /opt/acme /opt/acme-certs
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]