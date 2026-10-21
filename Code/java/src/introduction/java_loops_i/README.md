# Java Loops I

**Difficulty:** Easy · **Section:** Introduction · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-loops-i/problem)

---

**Objective**
In this challenge, we're going to use loops to help us do some simple math.

**Task**
Given an integer, $N$, print its first $10$ multiples. Each multiple $N \times i$ (where $1 \le i \le 10$) should be printed on a new line in the form: `N x i = result`.

**Input Format**

A single integer, $N$.

**Constraints**

- $2 \le N \le 20$

**Output Format**

Print $10$ lines of output; each line $i$ (where $1 \le i \le 10$) contains the $result$ of $N \times i$ in the form:
`N x i = result`.

**Sample Input**

```
2
```

**Sample Output**

```
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
```

## Solution

The part you write:

```java
for (int i = 1; i <= 10; i++) {
    System.out.println(N + " x " + i + " = " + (N * i));
}
```

- A `for` loop from 1 to 10 prints one line per multiple.
- Wrap `N * i` in parentheses so it is calculated before being joined to the text.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/introduction/java_loops_i/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
