<!-- study-layout -->
# Java BigInteger

🟢 **Easy** · 📁 **BigNumber** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-biginteger/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

In this problem, you have to add and multiply huge numbers! These numbers are so big that you can't contain them in any ordinary data types like a long integer.

Use the power of Java's BigInteger class and solve this problem.

## 📥 Input & output

### Input format

There will be two lines containing two numbers, $a$ and $b$.

### Constraints

$a$ and $b$ are non-negative integers and can have maximum $200$ digits.

### Output format

Output two lines. The first line should contain $a+b$, and the second line should contain $a \times b$. Don't print any leading zeros.

## 🧪 Example

**Input**

```
1234
20
```

**Output**

```
1254
24680
```

**Why**

1234 + 20 = 1254 and 1234 × 20 = 24680.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** `BigInteger` has no `+` or `*`: use the methods `add` and `multiply`.

### ✍️ The code you write

```java
Scanner sc = new Scanner(System.in);
BigInteger a = sc.nextBigInteger();
BigInteger b = sc.nextBigInteger();
sc.close();

System.out.println(a.add(b));        // a + b
System.out.println(a.multiply(b));   // a * b
```

### 🔍 How it works

- `Scanner.nextBigInteger()` reads a number of any size.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/bignumber/java_biginteger/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Primality Test](../java_primality_test/README.md) · [☕ All Java exercises](../../../README.md) · [Java 1D Array](../../data_structures/java_1d_array/README.md) ➡️
