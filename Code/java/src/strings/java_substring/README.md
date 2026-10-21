<!-- study-layout -->
# Java Substring

🟢 **Easy** · 📁 **Strings** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-substring/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Given a string, $s$, and two indices, $start$ and $end$, print a [substring](https://en.wikipedia.org/wiki/Substring) consisting of all characters in the inclusive range from $start$ to $end-1$. You'll find the *String* class' [substring method](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#substring-int-int-) helpful in completing this challenge.

## 📥 Input & output

### Input format

The first line contains a single string denoting $s$.
The second line contains two space-separated integers denoting the respective values of $start$ and $end$.

### Constraints

* $1 \le |s| \le 100$
* $0 \le start \lt end \le n$
- String $s$ consists of English alphabetic letters (i.e., $[a-zA-Z]$) only.

### Output format

Print the substring in the inclusive range from $start$ to $end-1$.

## 🧪 Example

**Input**

```
Helloworld
3 7
```

**Output**

```
lowo
```

**Why**

In the diagram below, the substring is highlighted in green:

| 0 | 1 | 2 | **3** | **4** | **5** | **6** | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| H | e | l | **l** | **o** | **w** | **o** | r | l | d |

*(highlighted in green on HackerRank: indexes 3 to 6, the substring `lowo`)*

## 💡 Solution

> [!TIP]
> **Key idea:** `substring(start, end)` includes `start` and stops **before** `end`, exactly the range asked for.

### ✍️ The code you write

```java
System.out.println(S.substring(start, end));   // end is excluded
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/strings/java_substring/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Strings Introduction](../java_strings_introduction/README.md) · [☕ All Java exercises](../../../README.md) · [Java Substring Comparisons](../java_substring_comparisons/README.md) ➡️
