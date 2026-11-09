#!/usr/bin/python

import sys
import os
argumentError = 'Invalid arguments supplied, must be run like (hb_script2_gpio.py x y) with 2>=x<=27 and y=[on,off]'

def get_flag(pin):
  return '/home/pi/homebridge_script2/flags/pin_' + str(pin) + '.flag'

def teleruptor_trigger(pin):
  import RPi.GPIO as GPIO
  import time
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin,GPIO.HIGH)
  time.sleep(.200)
  GPIO.output(pin,GPIO.LOW)

def teleruptor_on(pin):
  if os.path.exists(get_flag(pin)):
    return True
  else:
    return False

try:
    pin = sys.argv[1]
    action = sys.argv[2]
except IndexError:
    print argumentError

else:
  pin = int(pin)
  if len(sys.argv) == 3 and pin >= 2 and pin <= 27 and action in ['on', 'off']:

    if action == 'on':
      if not teleruptor_on(pin):
        teleruptor_trigger(pin)
        open(get_flag(pin), 'a').close()

    elif action == 'off':
      if teleruptor_on(pin):
        teleruptor_trigger(pin)
        os.remove(get_flag(pin))

  else:
    print argumentError
