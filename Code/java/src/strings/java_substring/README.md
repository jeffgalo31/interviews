# Java Substring

**Difficulty:** Easy · **Section:** Strings · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-substring/problem)

---

Given a string, $s$, and two indices, $start$ and $end$, print a [substring](https://en.wikipedia.org/wiki/Substring) consisting of all characters in the inclusive range from $start$ to $end-1$. You'll find the *String* class' [substring method](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#substring-int-int-) helpful in completing this challenge.

**Input Format**

The first line contains a single string denoting $s$.
The second line contains two space-separated integers denoting the respective values of $start$ and $end$.

**Constraints**

* $1 \le |s| \le 100$
* $0 \le start \lt end \le n$
- String $s$ consists of English alphabetic letters (i.e., $[a-zA-Z]$) only.

**Output Format**

Print the substring in the inclusive range from $start$ to $end-1$.

**Sample Input**

```
Helloworld
3 7
```

**Sample Output**

```
lowo
```

**Explanation**

In the diagram below, the substring is highlighted in green:

| 0 | 1 | 2 | **3** | **4** | **5** | **6** | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| H | e | l | **l** | **o** | **w** | **o** | r | l | d |

*(highlighted in green on HackerRank: indexes 3 to 6, the substring `lowo`)*

## Solution

The part you write:

```java
System.out.println(S.substring(start, end));   // end is excluded
```

- `substring(start, end)` includes `start` and stops **before** `end`, exactly the range asked for.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/strings/java_substring/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
