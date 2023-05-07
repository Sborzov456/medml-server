FROM nginx
WORKDIR /var/www/medml_front/

# COPY ./build/ .
# RUN npm install
# RUN npm start

# RUN mkdir -p /usr/src/web/static_files/front/
# COPY ./build/static/ /usr/src/web/static_files/front/
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
