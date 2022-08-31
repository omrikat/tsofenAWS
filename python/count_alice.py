
import os
from collections import Counter
FileName = "/home/parallels/workspace/tsofenAWS/python/Alice.txt"
fp = open(FileName,'r')
d = {}
#print(fp.read().split())
d = Counter(fp.read().split())
items = d.items()
max_word = []
for k,v in items:
    max_word.append(v)
for k,v in items:
    if(v == max(max_word)):
        print(k,v)
        break