import sys
# import network
# import socket
from utime import sleep, ticks_ms,ticks_diff
from machine import Pin,PWM,freq
import select
import math
machine.freq(125000000)
# import network
# import socket
global duty
duty=32768
global steps_per_revolution
steps_per_revolution=200
led = Pin("LED", Pin.OUT)

IN1x = Pin(2,Pin.OUT)#step
# IN1x.freq(1000)
# IN1x.duty_u16(duty)
# IN1x.deinit()
IN2x = Pin(3,Pin.OUT)#dir


IN1y = Pin(6,Pin.OUT)#step
# IN1y.freq(1000)
# IN1y.duty_u16(duty)
# IN1y.deinit()
IN2y = Pin(7,Pin.OUT)#dir


IN1z = Pin(10,Pin.OUT)#step
# IN1z.freq(1000)
# IN1z.duty_u16(duty)
# IN1z.deinit()
IN2z = Pin(11,Pin.OUT)#dir

global pinsx
global pinsy
global pinsz
pinsx = [IN1x, IN2x]

pinsy = [IN1y, IN2y]

pinsz = [IN1z, IN2z]
 
global pulse_x
global pulse_y
global pulse_z
pulse_x=0
pulse_y=0
pulse_z=0
def x_callback(pin):
#     if pin == IN1x:
    global pulse_x
    pulse_x+=1
    return pulse_x

def y_callback(pin):
#     if pin == IN1y:
    global pulse_y
    pulse_y+=1
    return pulse_y

def z_callback(pin):
#     if pin == IN1z:
    global pulse_z
    pulse_z+=1
    return pulse_z

def freq_set(x_step,y_step,z_step):
    global pulse_x
    global pulse_y
    global pulse_z
    pulse_x=0
    pulse_y=0
    pulse_z=0
    length=math.sqrt((x_step)**2+(y_step)**2+(z_step)**2)
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
    speed_factor=rel_speed_factor_x+rel_speed_factor_y+rel_speed_factor_z
    base_freq=400
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
    # time_needed=int(max(abs(x_step),abs(y_step),abs(z_step))/max(freq_x,freq_y,freq_z))*1000000
    # start_time = ticks_us()
    pins = [
        (IN1x, freq_x,2*abs(x_step)),   
        (IN1y, freq_y,2*abs(y_step)),   
        (IN1z, freq_z,2*abs(z_step)),  
    ]
    pin_states = [False] * len(pins)
    last_toggle_times = [0] * len(pins)
    oscillation_counts = [0] * len(pins)
    while True:
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

#     if x_step!=0:
#        IN1x.freq(freq_x)
#        IN1x.duty_u16(duty)
#        IN1x.irq(handler=x_callback, trigger=2)
#     if y_step!=0:
#        IN1y.freq(freq_y)
#        IN1y.duty_u16(duty)
#        IN1y.irq(handler=y_callback, trigger=2)
#     if z_step!=0:
#        IN1z.freq(freq_z)
#        IN1z.duty_u16(duty)
#        IN1z.irq(handler=z_callback, trigger=2)
#     while True:
#     # Get the current time in microseconds
#         # current_time = ticks_us()
#         if pulse_x>=abs(x_step):
#             IN1x.duty_u16(0)
#             IN1x.deinit()
#         if pulse_y>=abs(y_step):
#             IN1y.duty_u16(0)
#             IN1y.deinit()
#         if pulse_z>=abs(z_step):
#             IN1z.duty_u16(0)
#             IN1z.deinit()
#         if pulse_x>=x_step and pulse_y>=y_step and pulse_z>=z_step:
#             break
        # # Calculate the elapsed time
        # elapsed_time = current_time - start_time

        # Check if the desired time 't' has passed
        # if elapsed_time >= time_needed:
        #     break

    
    # IN1y.deinit()
    # IN1z.deinit()
    



def move(x_step,y_step,z_step):
#global current_position_x
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

    #control numbers for step count
    # control_x=0
    # control_y=0
    # control_z=0
    sleep(0.001)
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
            parts = command.split(" ")
            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])
            move(x_step=x, y_step=y, z_step=z)
            print("ok")
            led.value(0)
