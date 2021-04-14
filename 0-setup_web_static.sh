#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
echo "Hello" > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
chgrp -R ubuntu:ubuntu /data/
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /etc/nginx/html;
    index  index.html index.htm;
    
    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html index.htm;
    }    
    
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4/;
    }
    
    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;
    }

}" > /etc/nginx/sites-available/default
service nginx restart
