#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    pointsAlice=0
    pointsBob=0

    for i in range(0,len(a)):

        if a[i]>b[i]:
            pointsAlice=pointsAlice+1
        
        elif a[i]<b[i]:
            pointsBob=pointsBob+1
       
        else:
            pointsAlice=pointsAlice+0
            pointsBob=pointsBob+0
        

    return pointsAlice,pointsBob


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
