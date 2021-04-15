#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
apt-get update
apt-get install nginx -y
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo 'hola Atenea' > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex on;\n}\n' /etc/nginx/sites-available/default
service nginx restart
# apt-get update
# apt-get -y install nginx
# mkdir -p /data/web_static/releases/test
# mkdir -p /data/web_static/shared
# echo "Holberton School" > /data/web_static/releases/test/index.html
# ln -sf /data/web_static/releases/test /data/web_static/current
# chown -R ubuntu:ubuntu /data/
# sed -i '/listen 80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex on;\n}\n' /etc/nginx/sites-available/default
# service nginx restart
