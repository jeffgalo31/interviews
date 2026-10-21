<!-- study-layout -->
# Java Loops I

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-loops-i/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

### Objective

In this challenge, we're going to use loops to help us do some simple math.

### Task

Given an integer, $N$, print its first $10$ multiples. Each multiple $N \times i$ (where $1 \le i \le 10$) should be printed on a new line in the form: `N x i = result`.

## 📥 Input & output

### Input format

A single integer, $N$.

### Constraints

- $2 \le N \le 20$

### Output format

Print $10$ lines of output; each line $i$ (where $1 \le i \le 10$) contains the $result$ of $N \times i$ in the form:
`N x i = result`.

## 🧪 Example

**Input**

```
2
```

**Output**

```
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
```

## 💡 Solution

> [!TIP]
> **Key idea:** A `for` loop from 1 to 10 prints one line per multiple.

### ✍️ The code you write

```java
for (int i = 1; i <= 10; i++) {
    System.out.println(N + " x " + i + " = " + (N * i));
}
```

### 🔍 How it works

- Wrap `N * i` in parentheses so it is calculated before being joined to the text.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_loops_i/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Output Formatting](../java_output_formatting/README.md) · [☕ All Java exercises](../../../README.md) · [Java Loops II](../java_loops_ii/README.md) ➡️
