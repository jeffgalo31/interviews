# Java Output Formatting

**Difficulty:** Easy · **Section:** Introduction · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-output-formatting/problem)

---

Java's *System.out.printf* function can be used to print formatted output. The purpose of this exercise is to test your understanding of formatting output using *printf*.

To get you started, a portion of the solution is provided for you in the editor; you must format and print the input to complete the solution.

**Input Format**

Every line of input will contain a *String* followed by an *integer*.
Each *String* will have a maximum of $10$ alphabetic characters, and each *integer* will be in the inclusive range from $0$ to $999$.

**Output Format**

In each line of output there should be two columns:
The first column contains the *String* and is left justified using exactly $15$ characters.
The second column contains the *integer*, expressed in exactly $3$ digits; if the original input has less than three digits, you must pad your output's leading digits with zeroes.

**Sample Input**

```
java 100
cpp 65
python 50
```

**Sample Output**

```
================================
java           100
cpp            065
python         050
================================
```

**Explanation**

Each String is left-justified with trailing whitespace through the first 15 characters. The leading digit of the integer is the 16th character, and each integer that was less than 3 digits now has leading zeroes.

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

The part you write:

```java
System.out.printf("%-15s%03d%n", s1, x);
```

- `%-15s`: the string, left-justified (`-`) in a field 15 characters wide.
- `%03d`: the integer in 3 digits, padded with leading zeros (`0`).
- `%n`: a new line.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/introduction/java_output_formatting/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
