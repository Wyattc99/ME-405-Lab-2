"""!
@file plottingtask.py
This file configures Nucleo pins, timers, and channels for so that it can send voltage to a motor.
Can send a PWM duty cycle to the motor to control how fast the motor spins. Uses a L6206 motor shield to control motor direction.
@author Jacob Wong
@author Wyatt Conner
@author Jameson Spitz
@date   27-Jan-22
@copyright by Jameson Spitz all rights reserved
"""
import serial
import time

time_data = []
position = []

with serial.Serial('COM6', 115200) as s_port:
    #s_port.write (b'main()')
    #time.sleep(2)
    #s_port.write(b'0x04\r')
    time.sleep(2)
    s_port.write (b'16000\r')
    time.sleep(2)
    s_port.write (b'30\r')
    
    while True:
        position.append(s_port.readline().split (b','))
        
    print(position)
    
if __name__ == "__main__":
    print('Hello')
    #print(s_port)
    

