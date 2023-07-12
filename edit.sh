#!/bin/bash

edit=`mktemp --suffix=.conllu`
./pull_sentences.py $1 $2 $3 > $edit
emacs $edit
merge=`mktemp`
./push_sentences.py $1 $edit > $merge
mv $merge $1.conllu
