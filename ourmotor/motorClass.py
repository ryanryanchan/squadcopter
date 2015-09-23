#motor class

from RPIO import PWM

class motor(object):
#

    def __init__(self, pin, min = 0, max = 100):
        self.pin = pin
        # min, max, and power are all percentages
        self.min = min
        self.max = max
        self.power = 0
        #initializes a PWM class from RPIO that will be assigned to the motor
        self.PWM = PWM
        
    

    def start(self):
        if not self.PWM.is_setup():
            self.PWM.setup(pulse_incr_us=1)
            #logging
            #self.PWM.set_loglevel(PWM.LOG_LEVEL_ERRORS)
            #set granularity to 1 microsecond, pulse width to 3,000 us, 333.3Hz
            self.PWM.init_channel(1,3000)

    
    def setMin(self, min):
        self.min = min

    def setMax(self, max):
        self.max = max

    def getPower(self):
        return self.power

    def setPower(self, num):
        
        power = round(num,2)
        self.power = power
        
        if power < self.min:
            self.power = self.min
        if power > self.max:
            self.power = self.max
        
        scaled_power = 1055 + int(power*10)
        self.PWM.add_channel_pulse(1, self.pin, 0, scaled_power)

    def addPower(self, num):
        self.setPower(self.getPower() + num)

    def stop(self):
        self.power = 0
        self.PWM.cleanup()
