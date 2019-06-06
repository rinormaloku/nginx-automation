 #!/bin/bash

DOMAIN=$1

echo "Start: certificate creation"

certbot certonly --webroot -w /var/www/certs -d $DOMAIN 

if [ $? -ne 0 ]; then
  echo "Failed most likely confiugration of A record is not done correctly"
  exit 1
fi

echo "Completion: Certificate created"

cp /var/www/nginx-automation/www.sample.com.dev.conf /var/www/nginx-automation/nginx/$DOMAIN.conf

sed -i "s/DOMAIN_HOLDER/$DOMAIN/g" /var/www/nginx-automation/nginx/$DOMAIN.conf

mv /var/www/nginx-automation/nginx/$DOMAIN.conf /var/www/nginx-automation/nginx/domains/$DOMAIN.conf

docker kill -s HUP nginx
