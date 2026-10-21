<!-- study-layout -->
# Java String Reverse

🟢 **Easy** · 📁 **Strings** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-string-reverse/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.

***
Given a string $A$, print ``Yes`` if it is a palindrome, print ``No`` otherwise.

## 📥 Input & output

### Constraints

* $A$ will consist at most $50$ lower case english letters.

## 🧪 Example

**Input**

```
madam
```

**Output**

```
Yes
```

## 💡 Solution

> [!TIP]
> **Key idea:** `StringBuilder.reverse()` reverses the text.

### ✍️ The code you write

```java
String reversed = new StringBuilder(A).reverse().toString();
System.out.println(A.equals(reversed) ? "Yes" : "No");
```

### 🔍 How it works

- A palindrome equals its reverse; compare strings with `equals`, never `==`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/strings/java_string_reverse/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Substring Comparisons](../java_substring_comparisons/README.md) · [☕ All Java exercises](../../../README.md) · [Java Anagrams](../java_anagrams/README.md) ➡️
