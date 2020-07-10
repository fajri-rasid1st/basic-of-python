# Iterables and Iterators
import itertools


def find_probability(n, r):
    probability = [item for item in itertools.combinations(n, r) if "a" in item]
    return len(probability) / len(list(itertools.combinations(n, r)))


if __name__ == "__main__":
    useless = int(input())
    n = tuple(input().split())
    r = int(input())
    print(find_probability(n, r))
