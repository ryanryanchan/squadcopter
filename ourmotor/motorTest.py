#motor testor

#requires Python 1 or Python 2


from motorClass import motor


print('Enter BCM number: ')
pin = int(raw_input())

m1 = motor(pin)


print('Ensure ESC power is NOT connected.')
print('Press ENTER to start.')
input = raw_input()
m1.start()
#m1.setPower(100)
m1.PWM.add_channel_pulse(1,m1.pin,0,2999)
print('Wait for beepbeep.')
print('Then press ENTER.')
input = raw_input()
#m1.setPower(0)
m1.PWM.add_channel_pulse(1,m1.pin,0,1000)
print('Wait for 3 beeps, beeeeeep.')
print('Press ENTER to start.')
input = raw_input()


print('Increase: a    Decrease: s     Set Power: [percentage]  Exit: x')

runMotor = True
try:
    nums = set(['0','1','2','3','4','5','6','7','8','9','.'])
    while runMotor:
        cmd = raw_input()
        if set(cmd).issubset(nums):
            m1.setPower(float(cmd))
            
        elif cmd == 'a':
            m1.setPower(m1.getPower()+1)
           
        elif cmd == 's':
            m1.setPower(m1.getPower()-1)
            
        elif cmd == 'x':
            runMotor = False
        else:
            print('invalid command')

        print('Pow: {}'.format(m1.getPower()) )

finally:
    m1.stop()
    print('Exit Successful')
