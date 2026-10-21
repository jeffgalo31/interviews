<!-- study-layout -->
# Java Output Formatting

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-output-formatting/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Java's *System.out.printf* function can be used to print formatted output. The purpose of this exercise is to test your understanding of formatting output using *printf*.

To get you started, a portion of the solution is provided for you in the editor; you must format and print the input to complete the solution.

## 📥 Input & output

### Input format

Every line of input will contain a *String* followed by an *integer*.
Each *String* will have a maximum of $10$ alphabetic characters, and each *integer* will be in the inclusive range from $0$ to $999$.

### Output format

In each line of output there should be two columns:
The first column contains the *String* and is left justified using exactly $15$ characters.
The second column contains the *integer*, expressed in exactly $3$ digits; if the original input has less than three digits, you must pad your output's leading digits with zeroes.

## 🧪 Example

**Input**

```
java 100
cpp 65
python 50
```

**Output**

```
================================
java           100
cpp            065
python         050
================================
```

**Why**

Each String is left-justified with trailing whitespace through the first 15 characters. The leading digit of the integer is the 16th character, and each integer that was less than 3 digits now has leading zeroes.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** `%-15s`: the string, left-justified (`-`) in a field 15 characters wide.

### ✍️ The code you write

```java
System.out.printf("%-15s%03d%n", s1, x);
```

### 🔍 How it works

- `%03d`: the integer in 3 digits, padded with leading zeros (`0`).
- `%n`: a new line.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_output_formatting/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Stdin and Stdout II](../java_stdin_and_stdout_ii/README.md) · [☕ All Java exercises](../../../README.md) · [Java Loops I](../java_loops_i/README.md) ➡️
