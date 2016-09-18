# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO        #This enables use of the RaspberryPi's PGIO pins
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT) #set pin 21 to output
p = GPIO.PWM(21,50)        #set the PWM on pin 21 to 50%
p.start(0) 

var = 1
brightness = 50

try :

  while var == 1 :  # This constructs an infinite loop

    print 'Brightness is ', brightness

    test1 = raw_input('up, down, on or off? ')  #this is just a placeholder

    if test1 == 'up':
      if brightness - 10 >= 0 :
        brightness = brightness - 10
      else:
        print ('maxed out')
    elif test1 == 'down':
       brightness = brightness + 10
    elif test1 == 'on':
       brightness = 0
    elif test1 == 'off':
       brightness = 100
    else:
       print 'Try again'

    p.ChangeDutyCycle(brightness)

except KeyboardInterrupt:

  p.stop()

GPIO.cleanup()