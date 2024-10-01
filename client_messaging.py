#!/usr/bin/env pybricks-micropython

from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button

brick = EV3Brick()

SERVER = 'ev3dev'  

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

brick.screen.print('Establishing connection...')
client.connect(SERVER)
brick.screen.print('Connected!')



while True:

    pressed = brick.buttons.pressed()

    if pressed and Button.CENTER in pressed:
        mbox.send('play_sound')
        brick.screen.print('Sent: play_sound')
        wait(500) 
    
    mbox.wait() 
    received_message = mbox.read()
    brick.screen.print(received_message) 
    wait(2000)


    