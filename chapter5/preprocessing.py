import sys


args = sys.argv
input_file_name = args[1]
output_file_name = args[2]

with open(input_file_name, 'r')as f:
    text = f.readlines()

res = []
for t in text:
    t = t.strip()
    if t == '' or t == '一' or t == '十一':
        continue
    t = t.replace('　', '')
    res.append(t)

with open(output_file_name, 'w')as f:
    [f.write(r + '\n') for r in res]