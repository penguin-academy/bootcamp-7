#!/bin/bash 

sudo apt update
sudo apt full-upgrade

bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
#node-red admin init
sudo npm install --unsafe-perm -g node-dht-sensor
sudo sudo npm install --unsafe-perm -g node-red-contrib-dht-sensor
sudo systemctl enable nodered.service
npm install node-red-contrib-dht-sensor
npm install node-red-dashboard
