# HackerRank: Java 2D Array

**Type:** HackerRank Java challenge
**Source:** [Java 2D Array](https://www.hackerrank.com/challenges/java-2d-array/problem)
**Focus:** nested sequences, matrix traversal, boundary-safe indexing, negative values

## Exercise

Given a 6-by-6 sequence of integers, examine every contiguous 3-by-3 window. For each window, sum the seven cells in this shape:

```text
a b c
  d
e f g
```

Return the largest sum. A 6-by-6 matrix has 16 possible top-left positions. Print only the largest sum.

### Example Input

```text
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 2 2 2
0 0 0 0 2 0
0 0 0 2 2 2
```

### Expected Output

```text
14
```

The maximum is the bottom-right hourglass: `2 + 2 + 2 + 2 + 2 + 2 + 2 = 14`.

## Solution

This method matches the HackerRank Java stub's `List<List<Integer>>` representation. Initialize to `Integer.MIN_VALUE` because a valid answer can be negative.

```java
static int maxHourglassSum(List<List<Integer>> values) {
    int maximum = Integer.MIN_VALUE;

    for (int row = 0; row < values.size() - 2; row++) {
        for (int column = 0; column < values.get(row).size() - 2; column++) {
            int sum = values.get(row).get(column)
                    + values.get(row).get(column + 1)
                    + values.get(row).get(column + 2)
                    + values.get(row + 1).get(column + 1)
                    + values.get(row + 2).get(column)
                    + values.get(row + 2).get(column + 1)
                    + values.get(row + 2).get(column + 2);
            maximum = Math.max(maximum, sum);
        }
    }

    return maximum;
}
```

**Complexity:** For an $R \times C$ matrix, $O((R-2)(C-2))$ time and $O(1)$ extra space.

**Interview follow-ups:** What if the matrix is not square? What if values are all negative? How would you generalize the shape or guard against integer overflow for larger inputs?
