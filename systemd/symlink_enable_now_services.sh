#!/bin/sh

#sudo ln -s /home/pi/av_dev/av-gpio-test.service /etc/systemd/system/
sudo ln -s /home/pi/av_dev/systemd/av-motor.service /etc/systemd/system/
sudo ln -s /home/pi/av_dev/systemd/av-sudo-pulseaudio.service /etc/systemd/system/
sudo ln -s /home/pi/av_dev/systemd/av-voice.service /etc/systemd/system/

sudo systemctl daemon-reload

#sudo systemctl enable --now av-gpio-test
sudo systemctl enable --now av-motor
sudo systemctl enable --now av-sudo-pulseaudio
#sudo systemctl enable --now av-voice
