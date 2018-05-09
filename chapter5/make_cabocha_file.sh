#!/bin/sh

input_text='../neko.txt'
preprocessing_input_text='neko.txt.pre'

python preprocessing.py ${input_text} ${preprocessing_input_text}

cabocha -f1 ${preprocessing_input_text} > neko.txt.cabocha

rm ${preprocessing_input_text}