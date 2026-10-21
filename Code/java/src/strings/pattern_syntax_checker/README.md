# Pattern Syntax Checker

**Difficulty:** Easy · **Section:** Strings · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/pattern-syntax-checker/problem)

---

Using __Regex__, we can easily match or search for patterns in a text. Before searching for a pattern, we have to specify one using some well-defined syntax.

In this problem, you are given a pattern. You have to check whether the syntax of the given pattern is valid.

**Note**: In this problem, a regex is only valid if you can compile it using the  [Pattern.compile](http://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html#compile%28java.lang.String%29) method.

**Input Format**

The first line of input contains an integer $N$, denoting the number of test cases. The next $N$ lines contain a string of any printable characters representing the pattern of a regex.

**Output Format**

For each test case, print ``Valid`` if the syntax of the given pattern is correct. Otherwise, print ``Invalid``. Do not print the quotes.

**Sample Input**

```
3
([A-Z])(.+)
[AZ[a-z](a-z)
batcatpat(nat
```

**Sample Output**

```
Valid
Invalid
Invalid
```

## Solution

The part you write:

```java
try {
	Pattern.compile(pattern);
	System.out.println("Valid");
} catch (PatternSyntaxException e) {
	System.out.println("Invalid");
}
testCases--;
```

- The definition of valid is "`Pattern.compile` accepts it", so just try to compile.
- A bad pattern throws `PatternSyntaxException`; catch it and print `Invalid`.
- Don't forget `testCases--`, or the loop never ends.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/strings/pattern_syntax_checker/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
