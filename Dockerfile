FROM python:3.8-slim

RUN mkdir /var/www/ && mkdir /var/www/TRX/
WORKDIR /var/www/TRX/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /var/www/TRX/

RUN chown -R www-data:www-data /var/www/TRX/

# for running a production server, use docker-compose with prod.yml or prod-ssl.yml
CMD ["python3", "project.py", "runserver"]
