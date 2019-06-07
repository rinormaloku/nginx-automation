#!/bin/bash

DOMAIN=$1

echo "Start: certificate creation"

# certbot certonly --webroot -w /var/www/certs -d $DOMAIN
/var/custom/scripts/acme.sh --issue --domain $DOMAIN --webroot /opt/acme --cert-home /opt/acme-certs --log


if [ $? -ne 0 ]; then
  echo "Failed most likely configuration of A record is not done correctly"
  exit 1
fi

echo "Completion: Certificate created"

cp /app/files/www.sample.com.conf /var/www/nginx/domains/$DOMAIN.conf

sed -i "s/DOMAIN_HOLDER/$DOMAIN/g" /var/www/nginx/domains/$DOMAIN.conf

# docker kill -s HUP nginx