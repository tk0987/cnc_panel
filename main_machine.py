import sys
import network
import socket
from utime import sleep, ticks_ms,ticks_diff
from machine import Pin,PWM,freq
import select
import math
machine.freq(125000000)

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
    base_freq=800
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

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='picoCNC', password='picowcnc')

# Set up server
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8000))
    server.listen(1)
    print("Server initialized and listening on port 8000.")
except OSError as e:
    print(f"Failed to initialize server: {e}")
    server = None

while server:  # Ensure server is valid
    try:
        # Accept a client connection
        client, address = server.accept()
        print(f"Connection established with {address}")
        
        # Process client data
        try:
            data = client.recv(1024)
            if data:
                data = data.decode("utf-8")
                parts = data.strip().split(" ")
                print("Received data:", parts)

                # Parse and act upon received data
                
                x = int(parts[0])
                y = int(parts[1])
                z = int(parts[2])
                print('Processed:', x, y, z)
                move(x_step=x, y_step=y, z_step=z)

        except Exception as e:
            print(f"Error processing client data: {e}")
        # finally:
        #     client.close()
        #     print("Connection closed.")

    except OSError as e:
        print(f"Socket error: {e}")
        if e.errno == 9:  # EBADF
            print("Server socket invalid. Reinitializing...")
            try:
                server.close()
            except:
                pass
            try:
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind(('0.0.0.0', 8000))
                server.listen(1)
                print("Server reinitialized and listening on port 8000.")
            except OSError as e:
                print(f"Failed to reinitialize server: {e}")
                break
    except KeyboardInterrupt:
        print("Shutting down server.")
        try:
            server.close()
        except:
            pass
        break

