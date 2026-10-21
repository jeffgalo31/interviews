# Java Datatypes

**Difficulty:** Easy · **Section:** Introduction · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-datatypes/problem)

---

Java has 8 primitive data types; *char, boolean, byte, short, int, long, float, and double*. For this exercise, we'll work with the primitives used to hold integer values (*byte, short, int,* and *long*):

* A *byte* is an 8-bit signed integer.
* A *short* is a 16-bit signed integer.
* An *int* is a 32-bit signed integer.
* A *long* is a 64-bit signed integer.

Given an input integer, you must determine which primitive data types are capable of properly storing that input.

To get you started, a portion of the solution is provided for you in the editor.

**Reference:** https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html

**Input Format**

The first line contains an integer, $T$, denoting the number of test cases.
Each test case, $T$, is comprised of a single line with an integer, $n$, which can be arbitrarily large or small.

**Output Format**

For each input variable $n$ and appropriate primitive $dataType$, you must determine if the given primitives are capable of storing it. If yes, then print:

	n can be fitted in:
    * dataType

If there is more than one appropriate data type, print each one on its own line and order them by size (i.e.: $byte < short < int < long$).

If the number cannot be stored in one of the four aforementioned primitives, print the line:

	n can't be fitted anywhere.

**Sample Input**

```
5
-150
150000
1500000000
213333333333333333333333333333333333
-100000000000000
```

**Sample Output**

```
-150 can be fitted in:
* short
* int
* long
150000 can be fitted in:
* int
* long
1500000000 can be fitted in:
* int
* long
213333333333333333333333333333333333 can't be fitted anywhere.
-100000000000000 can be fitted in:
* long
```

**Explanation**

−150 can be stored in a short, an int, or a long.

213333333333333333333333333333333333 is very large and is outside of the allowable range of values for the primitive data types discussed in this problem.

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

The part you write:

```java
if (x >= Short.MIN_VALUE && x <= Short.MAX_VALUE) System.out.println("* short");
if (x >= Integer.MIN_VALUE && x <= Integer.MAX_VALUE) System.out.println("* int");
System.out.println("* long");   // nextLong() succeeded, so it always fits in a long
```

- Ranges: byte −128..127, short −32768..32767, int about ±2.1 billion, long about ±9.2 × 10^18.
- `Short.MIN_VALUE`, `Integer.MAX_VALUE`, ... avoid typing the limits by hand.
- If `nextLong()` throws, the number is too big even for a long, and the locked `catch` prints "can't be fitted anywhere".

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/introduction/java_datatypes/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
