<!-- study-layout -->
# Java Primality Test

🟢 **Easy** · 📁 **BigNumber** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-primality-test/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

A prime number is a natural number greater than $1$ whose only positive divisors are $1$ and itself. For example, the first six prime numbers are $2$, $3$, $5$, $7$, $11$, and $13$.

Given a large integer, $n$, use the Java *BigInteger* class' [*isProbablePrime*](https://docs.oracle.com/javase/7/docs/api/java/math/BigInteger.html#isProbablePrime%28int%29) method to determine and print whether it's ``prime`` or  ``not prime``.

## 📥 Input & output

### Input format

A single line containing an integer, $n$ (the number to be checked).

### Constraints

* $n$ contains at most $100$ digits.

### Output format

If $n$ is a prime number, print ``prime``; otherwise, print ``not prime``.

## 🧪 Example

**Input**

```
13
```

**Output**

```
prime
```

**Why**

The only positive divisors of 13 are 1 and 13, so we print `prime`.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** `BigInteger` handles numbers far bigger than `long` (up to 100 digits here).

### ✍️ The code you write

```java
boolean prime = new BigInteger(n.trim()).isProbablePrime(100);
System.out.println(prime ? "prime" : "not prime");
```

### 🔍 How it works

- `isProbablePrime(certainty)`: with certainty 100 the chance of a wrong "prime" is below 1 in 2^100.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/bignumber/java_primality_test/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java BigDecimal](../java_bigdecimal/README.md) · [☕ All Java exercises](../../../README.md) · [Java BigInteger](../java_biginteger/README.md) ➡️
