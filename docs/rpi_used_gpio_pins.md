for prototype 2

all numbers are GPIO pin numbers

lamps
- 17, 27, 22, 10, 9, 11
- front, right, left, top, back, brake

brake (linear actuator)
- 23, 24

geekworm battery hat wiki says:
- 2, 3, 5, 12, 13, 6, 20

output True several seconds for GPIO 26 pin will make rpi3 shutdown, not sure why
- 26

motor 3 pin connector (control speed?)
- 7, 21, 16
- CS, SCK, SDI/SDO

motor 2 pin connector
- 25

forward reverse switch
- two wires
    - 18
- three wires
    - 19

unused gpio pins (left and right based on <https://pinout.xyz>)
- left
    - 4, 0
- right
    - 14, 15, 8, 1

for raspberry pi 4 B, GPIO 0-8 are all pull high (default output 3.3V)

GPIO 14 seems defualt has 1V+, GPIO 15 seems default 3.3V, not sure why

maybe use a table for this doc?
