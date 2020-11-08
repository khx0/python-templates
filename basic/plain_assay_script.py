#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-11-08
# file: plain_assay_script.py
##########################################################################################

import sys
import os
import platform
import datetime
import numpy as np

today = datetime.datetime.now().strftime("%Y-%m-%d")
now   = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

os.makedirs(RAWDIR, exist_ok = True)
os.makedirs(OUTDIR, exist_ok = True)

if __name__ == '__main__':

    print(__file__, "running using python", platform.python_version())

    print("today: ", today)
    print("now: ", now)
