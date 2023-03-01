#bin/bash

echo "Updating"
sudo apt update
echo "Upgrading"
sudo apt upgrade
echo "Downloading autokey"
sudo apt install autokey-gtk
echo "Downloading OBS"
sudo apt install obs-studio
echo "Downloading Discord"
wget "https://discord.com/api/download?platform=linux&format=deb" -O discord.deb
sudo dpkg -i discord.deb
echo "Downloading Chrome"
wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" -O chrome.deb
sudo dpkg -i chrome.deb


sudo apt update
sudo apt upgrade