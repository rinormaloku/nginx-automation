# nginx-automation
Currently after running docker-compose all we have to do is execute auto.sh as root:

```
sudo bash auto.sh test.domain.com
```

ToDo:
- Each VM needs to restart nginx's

wget https://github.com/Neilpang/acme.sh/archive/2.8.1.zip | unzip -p 2.8.1.zip acme.sh-2.8.1/acme.sh > acme.sh