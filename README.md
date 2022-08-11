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

on the video receiver side computer (display the video onto big screen, not the computer on the car):
```sh
# default 3 cameras
./prototyp_1/video_receiver/ssh_ffmpeg_mpv.sh
# if use 4 cameras:
#./prototyp_1/video_receiver/ssh_ffmpeg_mpv.sh 4
```

./prototype_1/video_receiver/ssh_ffmpeg_mpv.sh only works on videos transfered from raspberry pi

./prototype_3/video_receiver/ssh_ffmpeg_mpv.sh is for nvidia jetson nano, it may not work, nvidia jetson nano names /dev/videox different from raspberry pi so I edited the script a little bit from prototype 1

you need to configure mdns on raspberry pi or jetson nano (the computer on the car)

you may need to ssh into the device and type yes for some prompt reguarding store fingerprint for the first time

you may need to remove /etc/.ssh/known_hosts if multiple computers has the same host name, you ssh into computer A before and want to ssh into computer B this time

some of these actions above can be solved with some flags/options/configs with ssh, so no need to worry about all the edge cases

## IMPORTANT!!!

the script put password in clear text with `sshpass` for convenient automation right now, later on you need to use `ssh-copy-id` and edit /etc/ssh/sshd_config to enable passwordless authentication for better security

# autostart

use systemd service files and symlink_enable_now_services.sh script in ./prototype_1/video_receiver/ to enable corresponding services

run scripts in .profile (.bash_profile) or .bashrc or .xinitrc or place for the display manager (different display manager has different methods to autostart which I am not familiar with)

<https://github.com/flyxyz123/dwm_av/tree/av> for auto put different videos transfered from remote computers at differnt "tags" (like workspaces), needs to compile and install, dependency requirements and other stuff see <https://dwm.suckless.org/>

# Nvidia Jetson Nano

need to change shebang to /usr/bin/xxx or env xxx

may need to change some package names to be installed in `voice_setup.sh`

the use of /dev/videox is differnt than raspberry pi, see `diff prototype_1/video_receiver/ssh_ffmpeg_mpv.sh prototype_3/video_receiver/ssh_ffmpeg_mpv.sh`

there are more problems I haven't solved, both voice and videos all seems not working correctly on Jetson Nano

# misc

if want to display video locally on computer on the car (raspberry pi, jetson nano), while transferring video to other computer, you need to use loop devices (loopback)

be careful about installing python packages with `pip`, python3 is preferrrd, but python2 may be the default, you need to configure the computer somehow to use python3 instead (like symlink /usr/bin/python to python3 instead of python2 and other stuff)
- raspberry pi has some packages like `python-is-python3` `python-dev-is-python3` for this purpose, which I put them into `voice_setup.sh`, but I remember that they do not work very well (not work as intended)
