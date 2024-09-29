#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

# Create an instance of the EV3Brick
brick = EV3Brick()

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# The server must be started before the client!
brick.screen.print('Waiting for connection...')
server.wait_for_connection()
brick.screen.print('Connected!')


mbox.wait()
received_message = mbox.read()
brick.screen.print(received_message)
wait(2000)
mbox.send('hello to you!')