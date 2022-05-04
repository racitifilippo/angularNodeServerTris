FROM debian

#RUN apt update && apt install -y apache2 iproute2 iputils-ping
RUN apt update && apt install -y nodejs

#COPY file /var/www/html
COPY node /home