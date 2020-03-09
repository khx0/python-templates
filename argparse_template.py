#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-02-29
# file: plain_assay_script.py
##########################################################################################

import sys
import datetime
import os
import numpy as np
import platform
import argparse

today = datetime.datetime.now().strftime("%Y-%m-%d")

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

os.makedirs(RAWDIR, exist_ok = True)
os.makedirs(OUTDIR, exist_ok = True)

def my_func(input, output, param = 1.0):

	print(input)

	print(output)

	return None

if __name__ == '__main__':
    
    print(__file__, "running using python", platform.python_version())

    input_file = './input_file.dat'

    output_file = './output_file.dat'

    parser = argparse.ArgumentParser(description = 'my_func function')

    parser.add_argument('-i', '--input', type = str, required = True,
    					help = 'input file')

    parser.add_argument('-o', '--output', type = str, required = True,
    					help = 'output file')


    args = parser.parse_args()

    print(args.input)
    print(args.output)

    # my_func(input = input_file,
    # 		output = output_file)
