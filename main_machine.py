import sys
# import network
# import socket
from time import sleep
from machine import Pin
import select
import math
# import network
# import socket

led = Pin("LED", Pin.OUT)

IN1x = Pin(2,Pin.OUT)#step
IN2x = Pin(3,Pin.OUT)#dir
# IN3x = Pin(4,Pin.IN, Pin.PULL_UP)#fault
#IN4x = Pin(5,Pin.OUT)

IN1y = Pin(6,Pin.OUT)#step
IN2y = Pin(7,Pin.OUT)#dir
# IN3y = Pin(8,Pin.IN, Pin.PULL_UP)#fault
#IN4y = Pin(9,Pin.OUT)

IN1z = Pin(10,Pin.OUT)#step
IN2z = Pin(11,Pin.OUT)#dir
# IN3z = Pin(12,Pin.IN, Pin.PULL_UP)#fault
#IN4z = Pin(13,Pin.OUT)
global steps_per_revolution
steps_per_revolution=200
# global current_position_x
# global current_position_y
# global current_position_z
global pinsx
global pinsy
global pinsz
pinsx = [IN1x, IN2x]

pinsy = [IN1y, IN2y]

pinsz = [IN1z, IN2z]
# current_position_x = 0
# current_position_y = 0
# current_position_z = 0


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
    length=math.sqrt((x_step)**2+(y_step)**2+(z_step)**2)
    rel_speed_factor_x=abs(x_step)/length
    rel_speed_factor_y=abs(y_step)/length
    rel_speed_factor_z=abs(z_step)/length
    speed_factor=rel_speed_factor_x+rel_speed_factor_y+rel_speed_factor_z
    #control numbers for step count
    control_x=0
    control_y=0
    control_z=0
    sleep(0.001)
    while True:
        if abs(x_step)==abs(y_step) and abs(x_step)==abs(z_step) and abs(z_step)==abs(y_step):
            if control_x < abs(x_step) and control_y < abs(y_step) and control_z < abs(z_step):

                pinsx[0].value(1)
                pinsy[0].value(1)
                pinsz[0].value(1)
                sleep(0.001)
                
                pinsx[0].value(0)
                pinsy[0].value(0)
                pinsz[0].value(0)
                
                sleep(0.001)
                
                control_x+=1
                control_y+=1
                control_z+=1
                
            if control_x<abs(x_step) and control_y<abs(y_step) and control_z>=abs(z_step):
                pinsx[0].value(1)
                pinsy[0].value(1)
                
                
                sleep(0.001)
                
                pinsx[0].value(0)
                pinsy[0].value(0)
                
                
                sleep(0.001)
                
                control_x+=1
                control_y+=1
                
            if control_x<abs(x_step) and control_y>=abs(y_step) and control_z<abs(z_step):
                pinsx[0].value(1)
                
                pinsz[0].value(1)
                
                sleep(0.001)
                
                pinsx[0].value(0)
                
                pinsz[0].value(0)
                
                sleep(0.001)
                
                control_x+=1
                
                control_z+=1

            if control_x>=abs(x_step) and control_y<abs(y_step) and control_z<abs(z_step):
                
                pinsy[0].value(1)
                pinsz[0].value(1)
                
                sleep(0.001)
                
                
                pinsy[0].value(0)
                pinsz[0].value(0)
                
                sleep(0.001)
                
                
                control_y+=1
                control_z+=1
                
            if control_x<abs(x_step) and control_y>=abs(y_step) and control_z>=abs(z_step):
                pinsx[0].value(1)
                
                
                sleep(0.001)
                
                pinsx[0].value(0)
                
                
                sleep(0.001)
                
                control_x+=1

            if control_x>=abs(x_step) and control_y<abs(y_step) and control_z>=abs(z_step):
                
                pinsy[0].value(1)
                
                
                sleep(0.001)
                
                
                pinsy[0].value(0)
                
                
                sleep(0.001)
                
                
                control_y+=1
                
            if control_x>=abs(x_step) and control_y>=abs(y_step) and control_z<abs(z_step):

                pinsz[0].value(1)
                
                sleep(0.001)
                

                pinsz[0].value(0)
                
                sleep(0.001)
                

                control_z+=1

        if abs(x_step)!=abs(y_step) or abs(x_step)!=abs(z_step) or abs(z_step)!=abs(y_step):
            if control_z<abs(z_step):
                pinsz[0].value(1)                
                sleep(0.0005/(rel_speed_factor_y/speed_factor))
                pinsz[0].value(0)
                sleep(0.0005/(rel_speed_factor_y/speed_factor))
                control_z+=1
            if control_y<abs(y_step):
                pinsy[0].value(1)                
                sleep(0.0005/(rel_speed_factor_y/speed_factor))
                pinsy[0].value(0)
                sleep(0.0005/(rel_speed_factor_y/speed_factor))
                control_y+=1
            if control_x<abs(x_step):
                pinsx[0].value(1)                
                sleep(0.0005/(rel_speed_factor_x/speed_factor))
                pinsx[0].value(0)
                sleep(0.0005/(rel_speed_factor_x/speed_factor))
                control_x+=1
        if control_x==abs(x_step) and control_z==abs(z_step) and control_y==abs(y_step):
            break

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



