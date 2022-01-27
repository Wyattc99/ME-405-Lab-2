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

with serial.Serial('COM27', 115200) as s_port:
    s_port.write(b'data')
    s_port.readline().split(b',')
    
