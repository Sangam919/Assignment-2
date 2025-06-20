import math
import os
import random
import re
import sys
def solve(s):
    result = []
    for word in s.split(' '):
        if word:
            result.append(word[0].upper() + word[1:])
        else:
            result.append('')
    return ' '.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
