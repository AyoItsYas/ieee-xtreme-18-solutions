import sys
import heapq


def main():
    input = sys.stdin.read
    data = input().splitlines()

    N, x = map(int, data[0].split())
    A = list(map(int, data[1].split()))

    A.sort()

    stacks = []

    for length in A:
        if stacks and stacks[0][0] + x <= length:
            top_length, stack = heapq.heappop(stacks)
            stack.append(length)
            heapq.heappush(stacks, (length, stack))
        else:
            new_stack = [length]
            heapq.heappush(stacks, (length, new_stack))

    print(len(stacks))
    for _, stack in stacks:
        print(len(stack), *sorted(stack, reverse=True))


if __name__ == "__main__":
    main()
