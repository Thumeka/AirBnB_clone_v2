#!/usr/bin/env bash
# Sets up the web server for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

#Create the folder /data/web_static/releases/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/

#Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

#Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir /data/web_static/releases/test

#Create a fake HTML file /data/web_static/releases/test/index.html w/ simple content
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee  /data/web_static/releases/test/index.html

#Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
#If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Give recursive ownership of the /data/ folder to the ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
#sudo sed -i '7i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
if [[ $(grep -c "location \/hbnb_static\/" /etc/nginx/sites-enabled/default) -eq 0 ]]
then
        sed -i "s/^\}$/\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/\;\n\t\}\n\}/" /etc/nginx/sites-enabled/default
fi

sudo service nginx start
