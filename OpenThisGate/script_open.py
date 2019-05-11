#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
#from OPi import GPIO
from time import sleep          # this lets us have a time delay

def open():
        cmd = "./on.sh"
        os.system(cmd)
        sleep(3)
        cmd = "./off.sh"
        os.system(cmd)