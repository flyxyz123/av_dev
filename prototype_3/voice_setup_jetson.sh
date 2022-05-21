#!/bin/sh
# may also need to change /usr/bin/python symlink from python2 to python3
# may need to install python-dev-is-python3 instead of python-dev

## from https://github.com/quangthanh010290/voice_control_using_raspberry
#sudo apt update
#yes | sudo apt upgrade
#
## misc
#yes | sudo apt install git python3-pip pulseaudio python-is-python3 python-dev-is-python3 
#
## voice
#yes | sudo apt install espeak libespeak1 portaudio19-dev libportaudio2 libportaudiocpp0 portaudio19-dev flac
## may need sudo pip install those packages if start voice program in sudo
## pyttsx3: text to speech library
#sudo pip install pyttsx3 PyAudio SpeechRecognition
#
## for usb mic array led
## more git clone stuff for mic array led see link
## https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/
##sudo pip install pyusb click
#
## from https://stackoverflow.com/a/64932897/9008720
## need if start as sudo
##sudo adduser root pulse-access
## need to run once per login
##sudo pulseaudio --system=true 0<&- >/dev/null 2>&1 &

yes | sudo apt-get install python3-pip python3-pyaudio
sudo pip3 install SpeechRecognition
