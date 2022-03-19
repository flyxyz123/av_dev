#!/bin/sh

sh -c 'sleep 3 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 320x240 -i /dev/video0 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --fs --title="video0" --profile=low-latency --demuxer=mkv -' &
sh -c 'sleep 3 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 320x240 -i /dev/video2 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --fs --title="video2" --profile=low-latency --demuxer=mkv -' &
sh -c 'sleep 3 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 320x240 -i /dev/video4 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --fs --title="video4" --profile=low-latency --demuxer=mkv -' &
