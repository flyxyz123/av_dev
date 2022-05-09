#!/bin/sh

# --autofit for ubuntu mpv version 0.32.0, arch this seems to be default
# Must specify `-c:v mjpeg` in input side. Else only one ffmpeg process is running if specify more than 320x240, all other ffmpeg processes just hang on rpi4, not sure why
# other maybe useful options:
# mpv: --untimed
# ffmpeg: -b:v 500k -maxrate 500k -minrate 500k

display_video () {
	sshpass -p agapeone ssh "$2" ffmpeg -an -f video4linux2 -s "$3" -c:v mjpeg -i "/dev/video$1" -c:v libx264 -preset ultrafast -tune zerolatency -f matroska - | mpv --autofit=100%x100% --fs --title="video$1" --profile=low-latency --demuxer=mkv -
	#sshpass -p agapeone ssh "pi@$2.local" ffmpeg -an -f video4linux2 -s "$3" -c:v mjpeg -i "/dev/video$1" -c:v copy -f matroska - | ffplay -
}

for i in $(seq "${1:-3}"); do
	sleep 1 && display_video $((0+(i-1)*2)) "${2:-pi@raspberrypi.local}" "${3:-1920x1080}" &
done
