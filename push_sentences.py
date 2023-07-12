#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('book', action='store')
parser.add_argument('merge', action='store')
args = parser.parse_args()

def getid(block):
    for line in block.splitlines():
        if 'sent_id' in line:
            return line.split()[-1]

merge = {}
with open(args.merge) as fin:
    for block in fin.read().rstrip().split('\n\n'):
        merge[getid(block)] = block

with open(f'{args.book}.conllu') as fin:
    for block in fin.read().rstrip().split('\n\n'):
        sid = getid(block)
        print(merge.get(sid, block), end='\n\n')
