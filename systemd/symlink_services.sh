#!/bin/sh

sudo ln -s /home/pi/av-gpio-test.service /etc/systemd/service/
sudo ln -s /home/pi/av-motor.service /etc/systemd/service/
sudo ln -s /home/pi/av-sudo-pulseaudio.service /etc/systemd/service/
sudo ln -s /home/pi/av-voice.service /etc/systemd/service/
sudo ln -s /home/pi/symlink_services.sh /etc/systemd/service/
