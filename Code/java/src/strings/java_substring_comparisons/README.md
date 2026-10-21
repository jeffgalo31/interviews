# Java Substring Comparisons

**Difficulty:** Easy · **Section:** Strings · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-string-compare/problem)

---

We define the following terms:

- [Lexicographical Order](https://en.wikipedia.org/wiki/Lexicographical_order), also known as *alphabetic* or *dictionary* order, orders characters as follows:
	$$\texttt{A} \lt \texttt{B} \lt \ldots \lt \texttt{Y} \lt \texttt{Z} \lt \texttt{a} \lt \texttt{b} \lt \ldots \lt \texttt{y} \lt \texttt{z}$$

    For example, `ball < cat`, `dog < dorm`, `Happy < happy`, `Zoo < ball`.
- A [substring](https://en.wikipedia.org/wiki/Substring) of a string is a contiguous block of characters in the string. For example, the substrings of `abc` are `a`, `b`, `c`, `ab`, `bc`, and `abc`.

Given a string, $s$, and an integer, $k$, complete the function so that it finds the lexicographically *smallest* and *largest* substrings of length $k$.

**Function Description**

Complete the *getSmallestAndLargest* function in the editor below.

*getSmallestAndLargest* has the following parameters:

- *string s:* a string
- *int k:* the length of the substrings to find

**Returns**

- *string:* the string '<smallest> + "\n" + <largest>' where <smallest> and <largest> are the two substrings

**Input Format**

The first line contains a string denoting $s$.
The second line contains an integer denoting $k$.

**Constraints**

- $1 \le |s| \le 1000$
- $s$ consists of English alphabetic letters only (i.e., `[a-zA-Z]`).

**Sample Input 0**

```
welcometojava
3
```

**Sample Output 0**

```
ava
wel
```

**Explanation**

String s = "welcometojava" has the following lexicographically-ordered substrings of length k = 3:

["ava", "com", "elc", "eto", "jav", "lco", "met", "oja", "ome", "toj", "wel"]

We then return the first (lexicographically smallest) substring and the last (lexicographically largest) substring as two newline-separated values (i.e., `ava\nwel`).

The stub code in the editor then prints `ava` as our first line of output and `wel` as our second line of output.

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

The part you write:

```java
public static String getSmallestAndLargest(String s, int k) {
    String smallest = s.substring(0, k);
    String largest = s.substring(0, k);

    // Every substring of length k starts at some index i from 0 to s.length() - k.
    for (int i = 1; i <= s.length() - k; i++) {
        String current = s.substring(i, i + k);
        if (current.compareTo(smallest) < 0) smallest = current;
        if (current.compareTo(largest) > 0) largest = current;
    }

    return smallest + "\n" + largest;
}
```

- Slide a window of length k over the string: `s.substring(i, i + k)` for every start index.
- Start both answers with the first window, then keep whichever compares smaller / larger (`compareTo`).
- Uppercase letters sort before lowercase (`Zoo < ball`), which `compareTo` already does.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/strings/java_substring_comparisons/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
