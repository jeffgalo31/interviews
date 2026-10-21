# Java Int to String

**Difficulty:** Easy · **Section:** Introduction · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-int-to-string/problem)

---

You are given an integer $n$, you have to convert it into a string.

Please complete the partially completed code in the editor. If your code successfully converts $n$ into a string $s$ the code will print "*Good job*". Otherwise it will print "*Wrong answer*".

$n$ can range between $-100$ to $100$ inclusive.

**Sample Input 0**

```
100
```

**Sample Output 0**

```
Good job
```

## Solution

The part you write:

```java
String s = Integer.toString(n);
```

- `Integer.toString(n)` (or `String.valueOf(n)`, or `"" + n`) converts the number to text.
- `DoNotTerminate` is HackerRank's guard against `System.exit`; it uses `SecurityManager`, which newer Java versions disabled, so the local version skips that call.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/introduction/java_int_to_string/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
