#!/usr/bin/env bash
# sets up web servers for web_static deployment

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server {/a \\tlocation \/hbnb_static\/ { alias \/data\/web_static\/current\/; index index.html; }' /etc/nginx/sites-enabled/default

sudo service nginx restart
