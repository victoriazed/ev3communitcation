#!/usr/bin/env pybricks-micropython

from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from pybricks.tools import wait
from pybricks.hubs import EV3Brick


brick = EV3Brick()

brick.speaker.beep()

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# The server must be started before the client!
brick.screen.print('Waiting for connection...')
server.wait_for_connection()
brick.screen.print('Connected!')

while True:

    mbox.wait()
    received_message = mbox.read()
    brick.screen.print(received_message)

    if received_message == 'play_sound':
        brick.speaker.beep()
        brick.screen.print('Playing sound!')
    