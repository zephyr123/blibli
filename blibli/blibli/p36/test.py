import os
import os.path
# with open('F:\\python_work\\blibli\\blibli\\p35\\something.txt','r') as f:
#     print(len(f.readlines()))
# file_name = 'F:\\python_work\\blibli\\blibli\\p35\\something.txt'
file_name = 'F:\\python_work\\blibli\\blibli\\p10\\p10-0.py'
lines = 0
with open(file_name,encoding='utf-8') as f:
    for each_line in f:
        lines += 1

print(lines)