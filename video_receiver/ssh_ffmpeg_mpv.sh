#!/bin/ssh

sh -c 'sleep 5 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 1920x1080 -i /dev/video0 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --title="video0" --profile=low-latency --untimed --demuxer=mkv -' &
sh -c 'sleep 5 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 1920x1080 -i /dev/video2 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --title="video2" --profile=low-latency --untimed --demuxer=mkv -' &
sh -c 'sleep 5 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 1920x1080 -i /dev/video4 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --title="video4" --profile=low-latency --untimed --demuxer=mkv -' &
sh -c 'sleep 5 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 1920x1080 -i /dev/video6 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --title="video6" --profile=low-latency --untimed --demuxer=mkv -' &
