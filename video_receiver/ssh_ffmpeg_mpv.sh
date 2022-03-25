#!/bin/sh

display_video () {
	sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 1920x1080 -c:v mjpeg -i "/dev/video$1" -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --autofit=100%x100% --fs --title="video$1" --profile=low-latency --demuxer=mkv -
}

# --autofit for ubuntu mpv version 0.32.0, arch this seems to be default
# Must specify `-c:v mjpeg` in input side. Else only one ffmpeg process is running if specify more than 320x240, all other ffmpeg processes just hang on rpi4, not sure why

#sh -c 'sleep 3 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 1920x1080 -c:v mjpeg -i /dev/video0 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --autofit=100%x100% --fs --title=video0 --profile=low-latency --demuxer=mkv -' &
#sh -c 'sleep 3 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 1920x1080 -c:v mjpeg -i /dev/video2 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --autofit=100%x100% --fs --title=video2 --profile=low-latency --demuxer=mkv -' &
#sh -c 'sleep 3 && sshpass -p raspberry ssh pi@raspberrypi.local ffmpeg -an -f video4linux2 -s 1920x1080 -c:v mjpeg -i /dev/video4 -r 30 -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --autofit=100%x100% --fs --title=video4 --profile=low-latency --demuxer=mkv -' &

# other useful options
# mpv: --untimed
# ffmpeg: -b:v 500k -maxrate 500k -minrate 500k

sleep 1 && display_video 0 &
sleep 1 && display_video 2 &
sleep 1 && display_video 4 &
