# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
english = set(map(int,input().split()))

b = int(input())
french = set(map(int,input().split()))

result = english.intersection(french)
print(len(result))
