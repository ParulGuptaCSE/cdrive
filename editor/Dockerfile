FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
COPY frontend.conf /etc/nginx/conf.d
COPY ./dist/ /var/www/frontend/
