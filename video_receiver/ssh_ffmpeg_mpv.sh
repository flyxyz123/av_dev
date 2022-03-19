#!/bin/sh

# --autofit for ubuntu mpv version 0.32.0, arch this seems to be default
sh -c 'sleep 3 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 320x240 -i /dev/video0 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --autofit=100%x100% --fs --title=video0 --profile=low-latency --demuxer=mkv -' &
sh -c 'sleep 3 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 320x240 -i /dev/video2 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --autofit=100%x100% --fs --title=video2 --profile=low-latency --demuxer=mkv -' &
sh -c 'sleep 3 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 320x240 -i /dev/video4 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --autofit=100%x100% --fs --title=video4 --profile=low-latency --demuxer=mkv -' &

# other useful options
# mpv: --untimed
# ffmpeg: -b:v 500k -maxrate 500k -minrate 500k
