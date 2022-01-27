"""!
@file postioncontrol.py
Control Motor's position
@author Jacob Wong
@author Wyatt Conner
@author Jameson Spitz
@date   27-Jan-22
@copyright by Jameson Spitz all rights reserved
"""
# from motordriver import MotorDriver
# from encoderdriver import EncoderDriver

class PositionControlTask():
    """!
    Task to control position
    """
    
    def __init__(self, Motor, Encoder):
        """!
        Intilizing Task
        """
        self.Motor = Motor
        self.Encoder = Encoder
        self.gain = 0
        self.setpoint = 0
        self.error = 0
    
    def set_point(self):
        """!
        Method that sets the position wanted
        """
        try:
            self.setpoint = float(input('Enter desired position value in ticks \n'))
            while self.setpoint == 0:
                self.setpoint = float(input('The set point cannot be zero enter a valid value \n'))
        except:
            print('Please enter a valid number for the set point')
            
    def set_gain(self):
        """!
        Method that sets the gain desired
        """
        try:
            self.gain = float(input('Enter desired porportional gain value \n'))
        except:
            print('Please enter a valid number for the gain')
    
    def position_control(self):
        """!
        Method to control position
        """
        # Update the encoder position
        self.Encoder.update_delta()
        
        self.position = self.Encoder.get_position()
        
        self.error = (-self.position + self.setpoint)/self.setpoint
        
        if self.error > 0:
            self.duty = self.gain*self.error + 15
        elif self.error < 0:
            self.duty = self.gain*self.error - 15
        else:
            self.duty = 0
        
        self.Motor.set_duty_cycle(self.duty)
    
    