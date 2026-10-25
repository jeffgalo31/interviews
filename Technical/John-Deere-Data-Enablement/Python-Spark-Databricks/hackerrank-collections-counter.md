# HackerRank: collections.Counter()

**Type:** HackerRank Python challenge
**Source:** [collections.Counter()](https://www.hackerrank.com/challenges/collections-counter/problem)
**Focus:** Python collections, frequency maps, consuming inventory

## Exercise

A shop has a limited number of shoes by size. For each customer request, sell a shoe only if the requested size remains in stock, then total the sale amounts.

Example input:

```text
6
6 6 4 5 6 4
4
6 55
6 45
4 40
5 30
```

Expected output:

```text
170
```

The inventory supports all four requests: $55 + $45 + $40 + $30 = $170.

## Solution

```python
from collections import Counter
import sys


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    index = 0

    shoe_count = values[index]
    index += 1
    stock = Counter(values[index:index + shoe_count])
    index += shoe_count

    customer_count = values[index]
    index += 1

    revenue = 0
    for _ in range(customer_count):
        size = values[index]
        price = values[index + 1]
        index += 2

        if stock[size] > 0:
            revenue += price
            stock[size] -= 1

    print(revenue)


if __name__ == "__main__":
    main()
```

**Complexity:** $O(n + c)$ time and $O(u)$ space, where $n$ is the number of shoes, $c$ the number of customers, and $u$ the number of distinct sizes.

**Check:** Stock `[6, 6]` and requests `(6, 55)`, `(6, 45)`, `(6, 55)` yield revenue `100`; the third request cannot be fulfilled.
