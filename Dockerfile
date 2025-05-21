FROM ubuntu
EXPOSE 80
RUN apt update
RUN apt install git -y
RUN apt install apache2 -y
RUN rm -rf /var/www/html/index.html
COPY startbootstrap-freelancer-gh-pages /var/www/html/
CMD apachectl -D FOREGROUND
