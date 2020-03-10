#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2020-03-10
# file: argparse_template.py
##########################################################################################

'''
example invocation
$python argparse_template.py -i ./input_file.dat -o ./output_file.dat
Type
$python argparse_template.py
to see the automatic help prompt provided by argparse.
Here, python denotes your default python interpreter on your system.
'''

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

def my_func(input, output, param = 1.0):
    '''
    dummy worker function
    '''
    print("input =", input)
    print("output =", output)

    assert os.path.isfile(input), f"Error: Input file {input} does not exist."

    cmd = f'touch {output}'
    os.system(cmd)

    ########################
    #                      #
    #     DO WORK HERE     #
    #                      #
    ########################

    return None

if __name__ == '__main__':

    print("running", __file__, "using python", platform.python_version())

    parser = argparse.ArgumentParser(description = 'my_func function')

    parser.add_argument('-i', '--input', type = str, 
                        required = True,
                        help = 'input file')

    parser.add_argument('-o', '--output', type = str,
                        required = True,
                        help = 'output file')

    args = parser.parse_args()

    my_func(input = args.input,
            output = args.output)

