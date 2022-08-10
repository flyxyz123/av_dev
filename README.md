# voice

some programs installed with ./prototype_x/voice_setup.sh may not be necessary

first time run voice.py:
```sh
./prototype_1/voice_setup.sh
./prototype_1/systemd/symlink_enable_now_services.sh
./prototype_2/voice.py
# if not working:
#sudo ./prototype_2/voice.py
```

after first time to run voice.py:
```
./prototype_2/voice.py
# if not working:
#sudo ./prototype_2/voice.py
```

# video

on the video receiver side computer (display the video onto big screen, not the computer on the car)
```sh
./prototyp_1/video_receiver/ssh_ffmpeg_mpv.sh
```
