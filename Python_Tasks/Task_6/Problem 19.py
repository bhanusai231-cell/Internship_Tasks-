# Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    from collections import Counter

count = Counter(s)

for char, frequency in sorted(count.items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(char, frequency)
