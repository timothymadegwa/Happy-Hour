#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = len(set(ar))
    vals =  dict(zip(set(ar),[0]*colors))
    for col in ar:
        vals[col]+=1
    socks = list(vals.values())
    pairs=0
    for p in socks:
        pairs+=int(p//2)
    
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
