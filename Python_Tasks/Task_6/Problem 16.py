# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
for i in range(A):
    n = int(input())
    a = set(map(int,input().split()))
    
    m = int(input())
    b = set(map(int,input().split()))
    print(a.issubset(b))
