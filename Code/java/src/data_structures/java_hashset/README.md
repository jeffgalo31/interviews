# Java Hashset

**Difficulty:** Easy · **Section:** Data Structures · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-hashset/problem)

---

In computer science, a set is an abstract data type that can store certain values, without any particular order, and no repeated values(Wikipedia). $\{1,2,3\}$ is an example of a set, but $\{1,2,2\}$ is not a set. Today you will learn how to use sets in java by solving this problem.<br>

You are given $n$ pairs of strings. Two pairs $(a,b)$ and $(c,d)$ are identical if $a=c$ and $b=d$. That also implies $(a,b)$ is *not* same as $(b,a)$. After taking each pair as input, you need to print number of unique pairs you currently have.

Complete the code in the editor to solve this problem.

**Input Format**

In the first line, there will be an integer $T$ denoting number of pairs. Each of the next $T$ lines will contain two strings seperated by a single space.

**Constraints:**

* $1 \le T \le 100000$
* Length of each string is atmost $5$ and will consist lower case letters only.

**Output Format**

Print $T$ lines. In the $i_{th}$ line, print number of unique pairs you have after taking $i^{th}$ pair as input.

**Sample Input**

```
5
john tom
john mary
john tom
mary anna
mary anna
```

**Sample Output**

```
1
2
2
3
3
```

**Explanation**

- After taking the first input, you have only one pair: (john,tom)
- After taking the second input, you have two pairs: (john, tom) and (john, mary)
- After taking the third input, you still have two unique pairs.
- After taking the fourth input, you have three unique pairs: (john,tom), (john, mary) and (mary, anna)
- After taking the fifth input, you still have three unique pairs.

## Solution

The part you write:

```java
Set<String> pairs = new HashSet<>();
for (int i = 0; i < t; i++) {
    pairs.add(pair_left[i] + " " + pair_right[i]);   // the space keeps ("ab","c") != ("a","bc")
    System.out.println(pairs.size());
}
```

- A `HashSet` ignores duplicates, so its size is the number of unique pairs so far.
- Join each pair into one string with a separator; order matters, so (a, b) and (b, a) stay different.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/data_structures/java_hashset/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
