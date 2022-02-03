"""!
@file main.py
This is the main file description
@author Jacob Wong
@author Wyatt Conner
@author Jameson Spitz
@date   2-Feb-22
@copyright by Jameson Spitz all rights reserved
"""
import motordriver
import encoderdriver
import positioncontrol
import time
import pyb

def main():
    """!
    The main program: All objects from each class are created here. 
    """
    
    ## Motor object instantiated from motor driver class.
    
    motor = motordriver.MotorDriver(pyb.Pin.board.PA0, pyb.Pin.board.PA1, pyb.Pin.board.PC1, 5)
    
    ## Encoder object instantiated from encoder class.
    
    encoder = encoderdriver.EncoderDriver(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    ## Controller object instatiated from PositionControl class.
    
    controller = positioncontrol.PositionControlTask(motor,encoder)
  
    ## Enables motors to pin.
    
    motor.enable()

    ## Prompts user to set a ticks set point.
    
    controller.set_point()
    
    ## Prompts user to set a controller gain.
    
    controller.set_gain()
    
    ## Creates list to store time data.
    
    time_list = []
    
    ## Creates list to store position data.
    
    position_list = []
    
    ## Initializes variable to store current time
    
    current_time = 0
    
    ## Sets start_time 
    
    start_time = time.ticks_ms()

    ## While loop that runs for 5 seconds
    while current_time <= 5_000:
        
        ## Runs position control function from positioncontrol.py
        
        controller.position_control()
        
        ## Updates Current Time
        
        current_time = time.ticks_diff(time.ticks_ms(), start_time)
        
        ## Updates motor speed every 10ms
        
        time.sleep_ms(10)
        
        ## Creates a list of Time data
        
        time_list.append(current_time)
        
        ## Creates a list of Time data
        position_list.append(encoder.get_position())
        
    print(time_list, position_list)
    
    ## Shuts off motor
    motor.set_duty_cycle(0)
    
    print('Done')
    
if __name__ == "__main__":
    main()
    
    