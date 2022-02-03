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
from matplotlib import pyplot

time_data = []
position = []


rows = []
data1 = [] 
data2 = []
string = ''
i = 0 
runs = 0
flag = False
num = False
newline = []
char = []
time_count = []
ticks = []

with serial.Serial('COM27', 115200) as s_port:
        time.sleep(.1)
        s_port.write(b'\x03')
        time.sleep(.1)
        s_port.write(b'\x04')
        time.sleep(.1)
        s_port.write (b'16000\r')
        time.sleep(.1)
        s_port.write (b'30\r')
        time.sleep(.5)
        s_port.reset_output_buffer()
        time.sleep(.1)
        s_port.read_until(b'30\r')
        time.sleep(.1)
        time.sleep(.1)
        data1 = s_port.read_until(b']')
        time.sleep(.1)
        data2 = s_port.read_until(b']')
        time.sleep(.1)
        data_string1 = data1.decode('Ascii')
        data_string2 = data2.decode('Ascii')
        
        data_string1.strip('\n')
        data_string1.strip(' ')
        data_string1.strip('[')
        data_string1.strip(']')
        
        data_string2.strip('\n')
        data_string2.strip(' ')
        data_string2.strip('[')
        data_string2.strip(']')
        
        for i in data_string1:
            if(i.isnumeric()):
                string += i
            elif(i == ',' or i == ']'):
                time_count.append(int(string)/1000)
                string = ''
        
        for i in data_string2:
            if(i.isnumeric()):
                string += i
            elif(i == ',' or i == ']'):
                ticks.append(int(string))
                string = ''
    
print('\nTime:\n', time_count)                      # Print data using pyplot
print('\nTicks:\n', ticks)
font = {'fontname':'Times New Roman'}
pyplot.plot(time_count, ticks, '-ok')
pyplot.title('Time vs Encoder Ticks', font)
pyplot.xlabel('Time, t [s]', font)
pyplot.ylabel('Encoder Ticks', font)
pyplot.grid()
if __name__ == "__main__":
    print('')
    #print(s_port)
    

