#!/bin/sh

#sudo ln -s /home/pi/av-gpio-test.service /etc/systemd/system/
sudo ln -s /home/pi/av-motor.service /etc/systemd/system/
sudo ln -s /home/pi/av-sudo-pulseaudio.service /etc/systemd/system/
sudo ln -s /home/pi/av-voice.service /etc/systemd/system/
sudo ln -s /home/pi/symlink_services.sh /etc/systemd/system/
