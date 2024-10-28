#!/bin/env python3


def transform_A_sequence(inputs, L):
    entries = []

    for direction, number in inputs:
        if direction == "U":
            entries.append((direction, L + number))
        elif direction == "R":
            entries.append((direction, L + (2 * L - number)))

    return sorted(set(entries), key=lambda x: x[1])


def transform_B_sequence(inputs, L):
    entries = []

    for direction, number in inputs:
        if direction == "L":
            entries.append((direction, number))
        elif direction == "U":
            entries.append((direction, number + L))

    return sorted(set(entries), key=lambda x: x[1])


def count_shapes(L, A, B):
    A = transform_A_sequence(A, L)
    B = transform_B_sequence(B, L)

    shapes = 1 + len(B)
    intersections = 0
    b_index = 0
    b_length = len(B)

    for direction_A, position_A in A:
        while b_index < b_length and position_A > B[b_index][1]:
            intersections += 1
            b_index += 1

        shapes += 1 + intersections

    return shapes


def main():
    L, N, M = map(int, input().split())
    A = [input().split() for _ in range(N)]
    B = [input().split() for _ in range(M)]

    A = [(x, int(y)) for x, y in A]
    B = [(x, int(y)) for x, y in B]

    print(count_shapes(L, A, B))


if __name__ == "__main__":
    main()
