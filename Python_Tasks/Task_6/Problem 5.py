# Write a Function
# https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap = True
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
    # Write your logic here
    

year = int(input())
print(is_leap(year))
