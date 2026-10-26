# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem
M = int(input())
A = set(map(int, input().split()))

N = int(input())
B = set(map(int, input().split()))

result = A.symmetric_difference(B)

for value in sorted(result):
    print(value)
