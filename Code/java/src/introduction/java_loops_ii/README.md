# Java Loops II

**Difficulty:** Easy · **Section:** Introduction · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-loops/problem)

---

We use the integers $a$, $b$, and $n$ to create the following series:

$$(a+2^{0} \cdot b), (a+2^{0} \cdot b + 2^{1} \cdot b), \ldots , (a + 2^{0} \cdot b+2^{1} \cdot b + \ldots + 2^{n-1} \cdot b)$$

You are given $q$ queries in the form of $a$, $b$, and $n$. For each query, print the series corresponding to the given $a$, $b$, and $n$ values as a single line of $n$ space-separated integers.

**Input Format**

The first line contains an integer, $q$, denoting the number of queries.
Each line $i$ of the $q$ subsequent lines contains three space-separated integers describing the respective $a_i$, $b_i$, and $n_i$ values for that query.

**Constraints**

* $0 \le q \le 500$
* $0 \le a, b \le 50$
* $1 \le n \le 15$

**Output Format**

For each query, print the corresponding series on a new line. Each series must be printed in order as a single line of $n$ space-separated integers.

**Sample Input**

```
2
0 2 10
5 3 5
```

**Sample Output**

```
2 6 14 30 62 126 254 510 1022 2046
8 14 26 50 98
```

**Explanation**

We have two queries:

1. We use a = 0, b = 2, and n = 10 to produce some series s0, s1, ..., s9:
   - s0 = 0 + 1·2 = 2
   - s1 = 0 + 1·2 + 2·2 = 6
   - s2 = 0 + 1·2 + 2·2 + 4·2 = 14

   ... and so on. Once we hit n = 10, we print the first ten terms as a single line of space-separated integers.

2. We use a = 5, b = 3, and n = 5 to produce some series s0, s1, ..., s4:
   - s0 = 5 + 1·3 = 8
   - s1 = 5 + 1·3 + 2·3 = 14
   - s2 = 5 + 1·3 + 2·3 + 4·3 = 26
   - s3 = 5 + 1·3 + 2·3 + 4·3 + 8·3 = 50
   - s4 = 5 + 1·3 + 2·3 + 4·3 + 8·3 + 16·3 = 98

   We then print each element of our series as a single line of space-separated values.

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

The part you write:

```java
StringBuilder line = new StringBuilder();
int value = a;
for (int j = 0; j < n; j++) {
    value += (1 << j) * b;        // add 2^j * b
    line.append(value);
    if (j < n - 1) line.append(' ');
}
System.out.println(line);
```

- Each term is the previous term plus `2^j * b`, so keep a running `value` instead of recomputing the sum.
- `1 << j` is 2 to the power j (shifting the bit 1 left j times).
- `StringBuilder` collects the numbers so the line is printed once, with spaces only between them.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/introduction/java_loops_ii/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
