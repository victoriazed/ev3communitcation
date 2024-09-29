#!/usr/bin/env pybricks-micropython

from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

brick = EV3Brick()

SERVER = 'ev3dev'  # Change this to the name of your server

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

brick.screen.print('Establishing connection...')
client.connect(SERVER)
brick.screen.print('Connected!')

# Use a loop to keep the client running
while True:
    mbox.send('hello!')
    mbox.wait() 
    received_message = mbox.read()
    brick.screen.print(received_message) 
    wait(2000)