<!-- study-layout -->
# Java If-Else

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-if-else/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Examples](#-examples) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

In this challenge, we test your knowledge of using *if-else* conditional statements to automate decision-making processes. An if-else statement has the following logical flow:

```
IF (A = TRUE)
Then B
Else C
End IF

          (start)
             |
             v
   TRUE <-- [ A ] --> FALSE
     |                  |
     v                  v
    [B]                [C]
     |                  |
     +------> (end) <---+
```

<sub>Source: [Wikipedia](https://en.wikipedia.org/wiki/Conditional_(computer_programming))</sub>

### Task

Given an integer, $n$, perform the following conditional actions:

* If $n$ is odd, print `Weird`
* If $n$ is even and in the inclusive range of $2$ to $5$, print `Not Weird`
* If $n$ is even and in the inclusive range of $6$ to $20$, print `Weird`
* If $n$ is even and greater than $20$, print `Not Weird`

Complete the stub code provided in your editor to print whether or not $n$ is weird.

## 📥 Input & output

### Input format

A single line containing a positive integer, $n$.

### Constraints

- $ 1 \le n \le 100$

### Output format

Print `Weird` if the number is weird; otherwise, print `Not Weird`.

## 🧪 Examples

### Example 1

**Input**

    3

**Output**

    Weird

### Example 2

**Input**

    24

**Output**

    Not Weird

## 💡 Solution

> [!TIP]
> **Key idea:** `N % 2 != 0` means N is odd (the remainder of dividing by 2 is not 0).

### ✍️ The code you write

```java
// Odd, or even between 6 and 20 -> Weird. Every other even number -> Not Weird.
if (N % 2 != 0 || (N >= 6 && N <= 20)) {
    System.out.println("Weird");
} else {
    System.out.println("Not Weird");
}
```

### 🔍 How it works

- The four rules collapse into one test: **Weird** if odd *or* between 6 and 20; otherwise **Not Weird**.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_if_else/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [ Java Stdin and Stdout I](../java_stdin_and_stdout_i/README.md) · [☕ All Java exercises](../../../README.md) · [Java Stdin and Stdout II](../java_stdin_and_stdout_ii/README.md) ➡️
