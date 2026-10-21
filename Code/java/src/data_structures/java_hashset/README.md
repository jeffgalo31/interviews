<!-- study-layout -->
# Java Hashset

🟢 **Easy** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-hashset/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

In computer science, a set is an abstract data type that can store certain values, without any particular order, and no repeated values(Wikipedia). $\{1,2,3\}$ is an example of a set, but $\{1,2,2\}$ is not a set. Today you will learn how to use sets in java by solving this problem.<br>

You are given $n$ pairs of strings. Two pairs $(a,b)$ and $(c,d)$ are identical if $a=c$ and $b=d$. That also implies $(a,b)$ is *not* same as $(b,a)$. After taking each pair as input, you need to print number of unique pairs you currently have.

Complete the code in the editor to solve this problem.

## 📥 Input & output

### Input format

In the first line, there will be an integer $T$ denoting number of pairs. Each of the next $T$ lines will contain two strings seperated by a single space.

### Constraints

* $1 \le T \le 100000$
* Length of each string is atmost $5$ and will consist lower case letters only.

### Output format

Print $T$ lines. In the $i_{th}$ line, print number of unique pairs you have after taking $i^{th}$ pair as input.

## 🧪 Example

**Input**

```
5
john tom
john mary
john tom
mary anna
mary anna
```

**Output**

```
1
2
2
3
3
```

**Why**

- After taking the first input, you have only one pair: (john,tom)
- After taking the second input, you have two pairs: (john, tom) and (john, mary)
- After taking the third input, you still have two unique pairs.
- After taking the fourth input, you have three unique pairs: (john,tom), (john, mary) and (mary, anna)
- After taking the fifth input, you still have three unique pairs.

## 💡 Solution

> [!TIP]
> **Key idea:** A `HashSet` ignores duplicates, so its size is the number of unique pairs so far.

### ✍️ The code you write

```java
Set<String> pairs = new HashSet<>();
for (int i = 0; i < t; i++) {
    pairs.add(pair_left[i] + " " + pair_right[i]);   // the space keeps ("ab","c") != ("a","bc")
    System.out.println(pairs.size());
}
```

### 🔍 How it works

- Join each pair into one string with a separator; order matters, so (a, b) and (b, a) stay different.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_hashset/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Stack](../java_stack/README.md) · [☕ All Java exercises](../../../README.md) · [Java Generics](../java_generics/README.md) ➡️
