# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
english = set(map(int,input().split()))

n = int(input())
french = set(map(int,input().split()))

result = english.union(french)
print(len(result))
