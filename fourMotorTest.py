#4 motor test

#requires Python 1 or Python 2

from motorClass import motor
from time import sleep

#using 25,24,4,18 (in order)

# get info for motor 1
print('Enter BCM number for motor 1: ')
pin = int(raw_input())
m1 = motor(pin)

# get info for motor 2
print('Enter BCM number for motor 2: ')
pin = int(raw_input())
m2 = motor(pin)

# get info for motor 3
print('Enter BCM number for motor 3: ')
pin = int(raw_input())
m3 = motor(pin)

# get info for motor 4
print('Enter BCM number for motor 4: ')
pin = int(raw_input())
m4 = motor(pin)


# array of all four motors
motors = [m1, m2, m3, m4]



# begin startup
print('Ensure ESC power is NOT connected.')
print('Press ENTER to start.')
input = raw_input()
for i in range(0,4):
    motors[i].start()
    sleep(1)
    motors[i].PWM.add_channel_pulse(1, motors[i].pin, 0, 2999)
    sleep(1)
print('Wait for beepbeep.')
print('Then press ENTER.')
input = raw_input()
for j in range(0,4):
    motors[j].PWM.add_channel_pulse(1, motors[i].pin, 0, 1000)
    sleep(1)
print('Wait for 2 beeps, beeeeeep.')
print('Press ENTER to start.')
input = raw_input()


print('Increase: a    Decrease: s     Set Power: [percentage]  Exit: x')


runMotor = True
try:
    nums = set(['0','1','2','3','4','5','6','7','8','9','.'])
    while runMotor:
        cmd = raw_input()
        if set(cmd).issubset(nums):
            for k in range(0,4):
                motors[k].setPower(float(cmd))
        
        elif cmd == 'a':
            for l in range(0,4):
                motors[l].setPower(motors[l].getPower()+1)
        
        elif cmd == 's':
            for m in range(0,4):
                motors[m].setPower(motors[m].getPower()-1)
        
        
        elif cmd == 'x':
            runMotor = False
        else:
            print('invalid command')
        
        print('Pow: {}'.format(motors[0].getPower()) )

finally:
    for n in range(0,4):
        motors[n].stop()
    print('Exit Successful')
