FROM nginx
WORKDIR /var/www/medml_front/

# RUN apt install npm

# COPY ./front_server .

# RUN mkdir -p /usr/src/web/static_files/front/
# COPY ./front_server/static/ /usr/src/web/static_files/front/
# RUN npm start
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
