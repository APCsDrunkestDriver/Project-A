#!/usr/bin/env python3.9.6

#requires python 3.9.6 and arcade 2.6.9
# to run python3 Pong.py
import arcade
import random
import tensorflow as tf
import time
from pathlib import Path
from left_paddle import left_paddle
from right_paddle import right_paddle
from ball import ball
from window import pong



#starts the game loop
game = pong()
arcade.run()
