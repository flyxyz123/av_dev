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

the script put password in clear text with `sshpass` for convenience, you should use `ssh-copy-id` and edit /etc/ssh/sshd_config to enable passwordless authentication for better security

# autostart

use systemd service files and symlink_enable_now_services.sh script in ./prototype_1/video_receiver/ to enable corresponding services

run scripts in .profile (.bash_profile) or .bashrc or .xinitrc or place for the display manager (different display manager has different methods to autostart which I am not familiar with)

<https://github.com/flyxyz123/dwm_av/tree/av> for auto put different videos transfered from remote computers at differnt "tags" (like workspaces), needs to compile and install, dependency requirements and other stuff see <https://dwm.suckless.org/>
