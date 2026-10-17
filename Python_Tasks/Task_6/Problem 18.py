# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int,input().split()))
N = int(input())
for _ in range(N):
    operation, size = input().split()
    other =set(map(int,input().split()))
    
    if operation == "update":
        A.update(other)
    elif operation == "intersection_update":
        A.intersection_update(other)
    elif operation == "difference_update":
        A.difference_update(other)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other)
print(sum(A))
