# Java String Reverse

**Difficulty:** Easy · **Section:** Strings · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-string-reverse/problem)

---

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.

***
Given a string $A$, print ``Yes`` if it is a palindrome, print ``No`` otherwise.

**Constraints**

* $A$ will consist at most $50$ lower case english letters.

**Sample Input**

```
madam
```

**Sample Output**

```
Yes
```

## Solution

The part you write:

```java
String reversed = new StringBuilder(A).reverse().toString();
System.out.println(A.equals(reversed) ? "Yes" : "No");
```

- `StringBuilder.reverse()` reverses the text.
- A palindrome equals its reverse; compare strings with `equals`, never `==`.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/strings/java_string_reverse/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
