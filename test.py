#!/usr/bin/env pybricks-micropython

from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button

brick = EV3Brick()

while True:

    pressed = brick.buttons.pressed()

    if pressed and Button.CENTER in pressed:
        brick.speaker.beep()