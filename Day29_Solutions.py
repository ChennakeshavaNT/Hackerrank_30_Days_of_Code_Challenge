#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        N = int(nk[0])

        K = int(nk[1])

        print(K-1 if ((K-1) | K) <= N else K-2)
