#!/bin/sh

#sudo ln -s /home/pi/av-gpio-test.service /etc/systemd/system/
sudo ln -s /home/pi/av_dev/systemd/av-motor.service /etc/systemd/system/
sudo ln -s /home/pi/av_dev/systemd/av-sudo-pulseaudio.service /etc/systemd/system/
sudo ln -s /home/pi/av_dev/systemd/av-voice.service /etc/systemd/system/
