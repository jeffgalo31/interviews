# Java BigDecimal

**Difficulty:** Medium · **Section:** BigNumber · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-bigdecimal/problem)

---

Java's BigDecimal class can handle arbitrary-precision signed decimal numbers. Let's test your knowledge of them!

Given an array, $s$, of $n$ real number strings, sort them in descending order &mdash; but wait, there's more! Each number must be printed in the exact same format as it was read from stdin, meaning that $.1$ is printed as $.1$, and $0.1$ is printed as $0.1$. If two numbers represent numerically equivalent values (e.g., $.1 \equiv 0.1$), then they must be listed in the same order as they were received as input).

Complete the code in the unlocked section of the editor below. You must rearrange array $s$'s elements according to the instructions above.

**Input Format**

The first line consists of a single integer, $n$, denoting the number of integer strings.
Each line $i$ of the $n$ subsequent lines contains a real number denoting the value of $s_i$.

**Constraints**

* $1 \le n \le 200$
* Each $s_i$ has *at most* $300$ digits.

**Output Format**

Locked stub code in the editor will print the contents of array $s$ to stdout. You are only responsible for reordering the array's elements.

**Sample Input**

```
9
-100
50
0
56.6
90
0.12
.12
02.34
000.000
```

**Sample Output**

```
90
56.6
50
02.34
0.12
.12
0
000.000
-100
```

## Solution

The part you write:

```java
// Sort only the first n entries (the array has 2 extra empty slots).
// Compare as numbers, largest first; keep the original strings so ".12" stays ".12".
Arrays.sort(s, 0, n, (a, b) -> new BigDecimal(b).compareTo(new BigDecimal(a)));
```

- Sort the **strings** but compare them as `BigDecimal` numbers, so each number is printed exactly as it was typed.
- `b.compareTo(a)` (reversed) gives descending order.
- `Arrays.sort` on objects is stable: equal values like `0.12` and `.12` keep their input order.
- Sort only indexes `0..n` because the array has 2 extra `null` slots.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/bignumber/java_bigdecimal/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
