FROM nginx:latest
MAINTAINER hide <sharehead@gmail.com>

COPY . ./home
WORKDIR home
RUN rm /etc/nginx/conf.d/default.conf
COPY ./docker/config/nginx.conf /etc/nginx/conf.d/default.conf