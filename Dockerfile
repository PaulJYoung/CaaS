FROM ubuntu:14.04

MAINTAINER Paul Young
RUN apt-get update
RUN apt-get install -y python python-pip python-dev 
RUN apt-get install -y libxml2-dev libxslt-dev libffi-dev libssl-dev 
RUN apt-get install -y libmysqlclient-dev

RUN mkdir /config
ADD /config/requirements.txt /config/
RUN pip install -r /config/requirements.txt
RUN mkdir /src
WORKDIR /src

EXPOSE 8000

#COPY ./config/caas_nginx.conf /etc/nginx/sites-available/
#COPY ./docker-entrypoint.sh /
#RUN ln -s /etc/nginx/sites-available/caas_nginx.conf /etc/nginx/sites-enabled
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf
#ENTRYPOINT ["/docker-entrypoint.sh"]
