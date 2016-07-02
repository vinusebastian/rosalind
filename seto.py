def print_set(S):
    print('{' + ", ".join(str(s) for s in S) + '}')
with open('seto_in.txt') as dataset:
     n = int(dataset.readline().rstrip())
     universe = set(range(1, n + 1))
     x = set((int(d) for d in dataset.readline()[1:-2].split(',')))
     y = set((int(d) for d in dataset.readline()[1:-2].split(',')))
     print_set(x | y)
     print_set(x & y)
     print_set(x - y)
     print_set(y - x)
     print_set(universe - x)
     print_set(universe - y)
