# Java BigInteger

**Difficulty:** Easy · **Section:** BigNumber · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-biginteger/problem)

---

In this problem, you have to add and multiply huge numbers! These numbers are so big that you can't contain them in any ordinary data types like a long integer.

Use the power of Java's BigInteger class and solve this problem.

**Input Format**

There will be two lines containing two numbers, $a$ and $b$.

**Constraints**

$a$ and $b$ are non-negative integers and can have maximum $200$ digits.

**Output Format**

Output two lines. The first line should contain $a+b$, and the second line should contain $a \times b$. Don't print any leading zeros.

**Sample Input**

```
1234
20
```

**Sample Output**

```
1254
24680
```

**Explanation**

1234 + 20 = 1254 and 1234 × 20 = 24680.

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

The part you write:

```java
Scanner sc = new Scanner(System.in);
BigInteger a = sc.nextBigInteger();
BigInteger b = sc.nextBigInteger();
sc.close();

System.out.println(a.add(b));        // a + b
System.out.println(a.multiply(b));   // a * b
```

- `BigInteger` has no `+` or `*`: use the methods `add` and `multiply`.
- `Scanner.nextBigInteger()` reads a number of any size.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/bignumber/java_biginteger/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
