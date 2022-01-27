"""!
@file main.py
This is the main file description
@author Jacob Wong
@author Wyatt Conner
@author Jameson Spitz
@date   27-Jan-22
@copyright by Jameson Spitz all rights reserved
"""
import motordriver
import encoderdriver
import positioncontrol
import time
import pyb

def main():
    motor = motordriver.MotorDriver(pyb.Pin.board.PA0, pyb.Pin.board.PA1, pyb.Pin.board.PC1, 5)
    encoder = encoderdriver.EncoderDriver(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    controller = positioncontrol.PositionControlTask(motor,encoder)
    
    motor.enable()

    controller.set_point()
    # 60 works well offset of 0
    # 30 works well offset of 10
    controller.set_gain()

    my_list = []
    current_time = 0
    start_time = time.ticks_ms()

    while current_time <= 5_000:
        controller.position_control()
        current_time = time.ticks_diff(time.ticks_ms(), start_time)
        time.sleep_ms(10)
        my_list.append([current_time, encoder.get_position()])
    print(my_list)
    motor.set_duty_cycle(0)
if __name__ == "__main__":
    main()
    
    