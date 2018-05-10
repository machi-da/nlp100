#!/bin/sh

file_name='knock45.txt'

#top10を表示
sort ${file_name} | uniq -c | sort -r | head -10

grep '^する\t' ${file_name} | sort | uniq -c | sort -r | head -n 10
grep '^見る\t' ${file_name} | sort | uniq -c | sort -r | head -n 10
grep '^与える\t' ${file_name} | sort | uniq -c | sort -r | head -n 10