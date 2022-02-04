#!/bin/sh
# may also need to change /usr/bin/python symlink from python2 to python3
# may need to install python-dev-is-python3 instead of python-dev

# from https://github.com/quangthanh010290/voice_control_using_raspberry
sudo apt update
yes | sudo apt upgrade
yes | sudo apt install espeak libespeak1 portaudio19-dev python-dev libportaudio2 libportaudiocpp0 portaudio19-dev python-gpiozero flac
# misc
yes | sudo apt install git

# may need sudo pip install those packages if start voice program in sudo
# pyttsx3: text to speech library
sudo pip install pyttsx3 PyAudio SpeechRecognition

# from https://stackoverflow.com/a/64932897/9008720
# need if start as sudo
#sudo adduser root pulse-access
#sudo pulseaudio --system=true 0<&- >/dev/null 2>&1 &

# for usb mic array led
sudo pip install pyusb
