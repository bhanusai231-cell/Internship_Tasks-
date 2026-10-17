# Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for _ in range(N):
    number = input()
    
    if re.fullmatch(r'[789]\d{9}', number):
        print("YES")
    else:
        print("NO")
