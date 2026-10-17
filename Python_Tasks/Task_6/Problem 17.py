# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))

n = int(input())

result = True

for _ in range(n):
    other = set(map(int, input().split()))

    if not A.issuperset(other):
        result = False
        break

print(result)
    
