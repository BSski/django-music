FROM python:3.9-buster

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/website
COPY requirements.txt start-server.sh /opt/app/
COPY website /opt/app/website/
WORKDIR /opt/app
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/app
RUN chmod 777 start-server.sh

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
