#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
apt-get update
if [ ! -x /usr/sbin/nginx ];
then
        apt-get install nginx -y
fi
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo 'hola Atenea' > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex off;\n}\n' /etc/nginx/sites-available/default
service nginx restart
