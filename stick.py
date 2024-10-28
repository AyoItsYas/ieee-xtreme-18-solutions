#!/bin/env python3


def main():
    N, K, L = map(int, input().split())

    single_square_area = (2 * L) ** 2

    if K > 2 * L:
        print(N * single_square_area)
    else:
        total_area = N * single_square_area - (N - 1) * (2 * L - K) ** 2
        print(total_area)


if __name__ == "__main__":
    main()
