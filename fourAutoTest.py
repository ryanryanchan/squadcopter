#auto motor test
#input correct gpio (25, 24, 4, 18)

from motorClass import motor
from time import sleep

TRIALS = 100
INCREMENT = 0.2
REST = 0.01

#Input the 4 GPIOS in the correct order
m1 = motor(int(raw_input('motor 1 GPIO: ')))
m2 = motor(int(raw_input('motor 2 GPIO: ')))
m3 = motor(int(raw_input('motor 3 GPIO: ')))
m4 = motor(int(raw_input('motor 4 GPIO: ')))

motors = [m1, m2, m3, m4]

raw_input('Make sure motors are unplugged')
for i in range(0, 4):
    motors[i].start()
    motors[i].setPower(100)

raw_input('Plug in, and then hit enter')

for i in range(0, 4):
    motors[i].PWM.add_channel_pulse(1,motors[i].pin, 0, 1000)
    sleep(1.5)
    motors[i].setPower(0)

for j in range(0,4):
    for i in range(TRIALS):
        motors[j].addPower(INCREMENT)
        print(str(motors[j].getPower())+'% ^')
        sleep(REST)


for j in range(0,4):
    for i in range(TRIALS):
        motors[j].addPower(-INCREMENT)
        print(str(motors[j].getPower())+'% v')
        sleep(REST)


for i in range(0, 4):
    motors[i].stop()

print('SUCCESS MOTHERFUCKER')
