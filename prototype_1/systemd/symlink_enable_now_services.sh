#!/bin/sh

#sudo ln -s /home/pi/av_dev/prototype_1/systemd/av-sudo-pulseaudio.service /etc/systemd/system/
sudo ln -s /home/pi/av_dev/prototype_1/systemd/av-motor.service /etc/systemd/system/
sudo ln -s /home/pi/av_dev/prototype_1/systemd/av-voice.service /etc/systemd/system/
sudo ln -s /home/pi/av_dev/prototype_1/systemd/av-camera-display.service /etc/systemd/system/

sudo systemctl daemon-reload

#sudo systemctl enable --now av-sudo-pulseaudio
sudo systemctl enable --now av-motor
sudo systemctl enable --now av-voice
sudo systemctl enable --now av-camera-display
