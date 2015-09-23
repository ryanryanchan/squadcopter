#auto motor test

from motorClass import motor
from time import sleep
#we use 25, 24, 4, 18

GPIO = 18
RANGE = 500
increment = .2
rest = .01

m1 = motor(GPIO)
m1.start()
raw_input('press enter')
m1.setPower(100)
raw_input('plug in, then hit enter')

m1.PWM.add_channel_pulse(1,GPIO,0,1000)
raw_input('enter when ready to go')
m1.setPower(0)

for i in range(RANGE):
    m1.addPower(increment)
    print(str(m1.getPower())+'% ^')
    sleep(rest)

sleep(1)

for i in range(RANGE + 1):
    m1.addPower(-increment)
    print(str(m1.getPower())+'% v')
    sleep(rest)
    
m1.stop()
print('SUCCESS MOTHERFUCKER')

  
