#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
#from OPi import GPIO
from time import sleep          # this lets us have a time delay

def open():
        cmd = "/root/OpenThisGate/OpenThisGate/on.sh"
        os.system(cmd)
        sleep(4)
        cmd = "/root/OpenThisGate/OpenThisGate/off.sh"
        os.system(cmd)
