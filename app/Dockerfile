FROM python:3.6.6-alpine
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]