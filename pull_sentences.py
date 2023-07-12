#!/usr/bin/env python3

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('book', action='store')
parser.add_argument('v1', action='store')
parser.add_argument('v2', action='store')
args = parser.parse_args()

def mkid(v):
    ch, vs = v.split(':')
    if len(ch) == 1:
        ch = '0' + ch
    return re.compile(f'{ch}_v{vs}[\n\\+]')

v1 = mkid(args.v1)
v2 = mkid(args.v2)

with open(f'{args.book}.conllu') as fin:
    printing = False
    for block in fin.read().split('\n\n'):
        if v1.search(block):
            printing = True
        if printing:
            print(block, end='\n\n')
        if v2.search(block):
            break
