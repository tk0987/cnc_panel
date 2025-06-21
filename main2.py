'''
its not used now in the project. this code is intended to drive psu - 3 transistors that control an EDM spark.
currently my psu is just a rectifier bridge with capacitor limiting the current to 7.5 A - before bridge, plus a fev milifarads (paralell now) after the bridge.
the amount of power is ok, but seems to damage the material (not only cutting but also damage). psu with transistors will be rebuild, then this code may become usefull again
'''

from machine import Pin, ADC
import utime
machine.freq(125000000)
# Constants
FREQ = 1000
PERIOD_US = int(1_000_000 / FREQ)  # 200 µs
adc = ADC(28)  # Potentiometer on GP26

# Setup GPIO pins
pins = [Pin(i, Pin.OUT) for i in (18, 19, 20)]

def get_duty_us():
    # Read potentiometer and convert to duty in microseconds
    val = adc.read_u16()
    # Map to 0.01% to 5% of 200 us => 0.02 us to 10 us
    min_us = PERIOD_US * 0.001  # 0.02 us
    max_us = PERIOD_US * 0.1    # 10 us
    return min_us + (val / 65535) * (max_us - min_us)

while True:
    duty_us = get_duty_us()

    # Stagger time between turn-on events
    step_delay = (PERIOD_US - duty_us) / 3

    t_start = utime.ticks_us()

    # Pin 18 ON
    pins[0].value(1)
    utime.sleep_us(int(step_delay))
    
    # Pin 19 ON
    pins[1].value(1)
    utime.sleep_us(int(step_delay))

    # Pin 20 ON
    pins[2].value(1)

    # Wait until common OFF time
    elapsed = utime.ticks_diff(utime.ticks_us(), t_start)
    remaining = max(0, int(PERIOD_US - duty_us - elapsed))
    utime.sleep_us(remaining)

    # All OFF
    for p in pins:
        p.value(0)

    # Wait for remaining time of the cycle
    elapsed = utime.ticks_diff(utime.ticks_us(), t_start)
    if elapsed < PERIOD_US:
        utime.sleep_us(PERIOD_US - elapsed)

