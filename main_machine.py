# this code was written for raspberry pi pico 
# i do not want to rewrite sth like grbl, so my pc does everything
# smooth enough

import sys
# import network
# import socket
from utime import sleep, ticks_ms,ticks_diff
from machine import Pin,PWM,freq
import select
import math
machine.freq(125000000)
# import network
# import socket #those later

global steps_per_revolution
steps_per_revolution=200
led = Pin("LED", Pin.OUT)

IN1x = Pin(2,Pin.OUT)#step

IN2x = Pin(3,Pin.OUT)#dir


IN1y = Pin(6,Pin.OUT)#step

IN2y = Pin(7,Pin.OUT)#dir


IN1z = Pin(10,Pin.OUT)#step

IN2z = Pin(11,Pin.OUT)#dir

global pinsx
global pinsy
global pinsz
pinsx = [IN1x, IN2x]

pinsy = [IN1y, IN2y]

pinsz = [IN1z, IN2z]
 

def freq_set(x_step,y_step,z_step):
    length=abs(x_step)+abs(y_step)+abs(z_step) # now normalised correctly...
    if x_step!=0:
        rel_speed_factor_x=abs(x_step)/length
    else:
        rel_speed_factor_x=0
    if y_step!=0:
        rel_speed_factor_y=abs(y_step)/length
    else:
        rel_speed_factor_y=0
    if z_step!=0:
        rel_speed_factor_z=abs(z_step)/length
    else:
        rel_speed_factor_z=0
   
 
    base_freq=1000 # i have weak engines - 5 rpm is even too much
 # what's more - this code is working, but engines can move faster. note - if, let's say, x=y and z=0, then x&y move with 500 Hz freq. and they can move with 1000 Hz each other
    if x_step!=0:
        freq_x=int(base_freq*(rel_speed_factor_x))
    else:
        freq_x=0
    if y_step!=0:
        freq_y=int(base_freq*(rel_speed_factor_y))
    else:
        freq_y=0
    if z_step!=0:
        freq_z=int(base_freq*(rel_speed_factor_z))
    else:
        freq_z=0

    pin_states = [False] * len(pins)
    last_toggle_times = [0] * len(pins)
    oscillation_counts = [0] * len(pins)
    while True: # this loop, with help of chatgpt 3.5, moves engines semi-asynchronously. they have diffrent frequencies (as pathlengths are different), but they need to finish their work together (for gcode).
        current_time = ticks_ms()

        for i, (pin, frequency, max_oscillations) in enumerate(pins):
            if oscillation_counts[i] < max_oscillations:
                if ticks_diff(current_time, last_toggle_times[i]) >= 1000 / frequency:
                    pin_states[i] = not pin_states[i]
                    pin.value(pin_states[i])
                    last_toggle_times[i] = current_time
                    oscillation_counts[i] += 1
        if all(oc >= max_oscillations for oc, _, max_oscillations in zip(oscillation_counts, pins, [max_oscillations for _, _, max_oscillations in pins])):
            break


def move(x_step,y_step,z_step):
#global current_position_x      #those 'current positions' will be used when i will have money for absolute coordinates. you know - all of those encoders and 'krańcówki'. and time (time is money).
#global current_position_y
#global current_position_z
    global pinsx
    global pinsy
    global pinsz
    #direction determination below!!!
    if x_step>=0:
        pinsx[1].value(1)
    if x_step<0:
        pinsx[1].value(0)
        
    if y_step>=0:
        pinsy[1].value(1)
    if y_step<0:
        pinsy[1].value(0)
        
    if z_step>=0:
        pinsz[1].value(1)
    if z_step<0:
        pinsz[1].value(0)

    sleep(0.0005) # work cannot wait
    freq_set(x_step,y_step,z_step)
 

while True:
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        a = sys.stdin.readline().strip()
        if len(a) > 0:
            led.value(1)
            command = a
#             if len(command) <= 1:
#                 reset_position()
#                 print("ok")
#             else:
            parts = command.split(" ")# single space - pc app uses three spaces. it is 'todo'. niby małe g(...), ale upierdliwe przy edycji
            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])
            move(x_step=x, y_step=y, z_step=z)
            print("ok") # for the pc app
            led.value(0)
