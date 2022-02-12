#!/bin/sh

sudo pulseaudio --system=true 0<&- >/dev/null 2>&1 &
