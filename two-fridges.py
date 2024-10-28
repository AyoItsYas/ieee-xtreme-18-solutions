#!/bin/env python3


def main():
    N = int(input())

    intervals = []
    for _ in range(N):
        a, b = map(int, input().split())
        intervals.append((a, b))

    for t1 in range(-100, 101):
        for t2 in range(t1, 101):
            valid = True
            for a, b in intervals:
                if not ((a <= t1 <= b) or (a <= t2 <= b)):
                    valid = False
                    break
            if valid:
                print(t1, t2)
                return

    print(-1)


if __name__ == "__main__":
    main()
