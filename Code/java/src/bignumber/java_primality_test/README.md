# Java Primality Test

**Difficulty:** Easy · **Section:** BigNumber · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-primality-test/problem)

---

A prime number is a natural number greater than $1$ whose only positive divisors are $1$ and itself. For example, the first six prime numbers are $2$, $3$, $5$, $7$, $11$, and $13$.

Given a large integer, $n$, use the Java *BigInteger* class' [*isProbablePrime*](https://docs.oracle.com/javase/7/docs/api/java/math/BigInteger.html#isProbablePrime%28int%29) method to determine and print whether it's ``prime`` or  ``not prime``.

**Input Format**

A single line containing an integer, $n$ (the number to be checked).

**Constraints**

* $n$ contains at most $100$ digits.

**Output Format**

If $n$ is a prime number, print ``prime``; otherwise, print ``not prime``.

**Sample Input**

```
13
```

**Sample Output**

```
prime
```

**Explanation**

The only positive divisors of 13 are 1 and 13, so we print `prime`.

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

The part you write:

```java
boolean prime = new BigInteger(n.trim()).isProbablePrime(100);
System.out.println(prime ? "prime" : "not prime");
```

- `BigInteger` handles numbers far bigger than `long` (up to 100 digits here).
- `isProbablePrime(certainty)`: with certainty 100 the chance of a wrong "prime" is below 1 in 2^100.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/bignumber/java_primality_test/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
