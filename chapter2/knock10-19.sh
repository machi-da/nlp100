#!/bin/sh

function knock10() {
    wc -l $1 | sed -E 's/^ *([0-9]+) .*/\1/'
}

function knock11() {
    cat $1 | tr '\t' ' '
}

function knock12() {
    cut -f1 $1 > col1_c.txt
    cut -f2 $1 > col2_c.txt
}

function knock13() {
    paste col1_c.txt col2_c.txt > merge_c.txt
}

function knock14() {
    head -$2 $1
}

function knock15() {
    tail -$2 $1
}

function knock16() {
    split -l $2 $1 $1
}

function knock17() {
    cut -f1 $1 | sort | uniq
}

function knock18() {
    sort -r -nk3 $1
}

function knock19() {
    cut -f1 $1 | sort | uniq -c | sort -r
}

file_name='knock10-19/hightemp.txt'
n=5

# 実行しないものは適宜コメント化
knock10 ${file_name}
knock11 ${file_name}
knock12 ${file_name}
knock13
knock14 ${file_name} ${n}
knock15 ${file_name} ${n}
knock16 ${file_name} ${n}
knock17 ${file_name}
knock18 ${file_name}
knock19 ${file_name}
