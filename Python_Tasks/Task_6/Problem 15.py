# Set .difference() Operation
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
english = set(map(int,input().split()))

b = int(input())
french = set(map(int,input().split()))

result = english.difference(french)
print(len(result))
