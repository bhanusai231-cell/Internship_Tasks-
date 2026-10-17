# Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem
N, M = map(int, input().split())

for i in range(N):
    if i < N // 2:
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))
    elif i == N // 2:
        print("WELCOME".center(M, "-"))
    else:
        pattern = ".|." * (2 * (N - i - 1) + 1)
        print(pattern.center(M, "-"))
