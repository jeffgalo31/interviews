<!-- study-layout -->
# Java Stdin and Stdout II

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-stdin-stdout/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

In this challenge, you must read an *integer*, a *double*, and a *String* from stdin, then print the values according to the instructions in the *Output Format* section below. To make the problem a little easier, a portion of the code is provided for you in the editor.

**Note:** We recommend completing [Java Stdin and Stdout I](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1) before attempting this challenge.

## 📥 Input & output

### Input format

There are three lines of input:

1. The first line contains an *integer*.
2. The second line contains a *double*.
3. The third line contains a *String*.

### Output format

There are three lines of output:

1. On the first line, print `String: ` followed by the unaltered *String* read from stdin.
2. On the second line, print `Double: ` followed by the unaltered *double* read from stdin.
3. On the third line, print `Int: ` followed by the unaltered *integer* read from stdin.

To make the problem easier, a portion of the code is already provided in the editor.

**Note:** If you use the *nextLine()* method immediately following the *nextInt()* method, recall that *nextInt()* reads integer tokens; because of this, the last newline character for that line of integer input is still queued in the input buffer and the next *nextLine()* will be reading the remainder of the integer line (which is empty).

## 🧪 Example

**Input**

```
42
3.1415
Welcome to HackerRank's Java tutorials!
```

**Output**

```
String: Welcome to HackerRank's Java tutorials!
Double: 3.1415
Int: 42
```

## 💡 Solution

> [!TIP]
> **Key idea:** `nextInt()` / `nextDouble()` read one token and leave the rest of the line (the newline) unread.

### ✍️ The code you write

```java
double d = scan.nextDouble();
scan.nextLine();              // finish the double's line (only its newline is left)
String s = scan.nextLine();   // the whole third line, spaces included
```

### 🔍 How it works

- So call `nextLine()` once to consume that leftover newline, then `nextLine()` again to read the sentence.
- `nextLine()` keeps spaces; `next()` would stop at the first space.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_stdin_and_stdout_ii/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java If-Else](../java_if_else/README.md) · [☕ All Java exercises](../../../README.md) · [Java Output Formatting](../java_output_formatting/README.md) ➡️
