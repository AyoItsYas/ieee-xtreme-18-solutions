#!/bin/env python3

import sys
import heapq
from collections import defaultdict


def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    group_ids = list(map(int, sys.stdin.readline().strip().split()))

    adj = defaultdict(list)
    in_degree = [0] * N

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        adj[a - 1].append(b - 1)
        in_degree[b - 1] += 1

    min_heap = []
    for i in range(N):
        if in_degree[i] == 0:
            heapq.heappush(min_heap, (group_ids[i], i))

    result = []
    while min_heap:
        _, project = heapq.heappop(min_heap)
        result.append(project + 1)

        for neighbor in adj[project]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(min_heap, (group_ids[neighbor], neighbor))

    if len(result) != N:
        print(-1)
    else:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
