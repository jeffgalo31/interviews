<!-- study-layout -->
# Java Int to String

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-int-to-string/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are given an integer $n$, you have to convert it into a string.

Please complete the partially completed code in the editor. If your code successfully converts $n$ into a string $s$ the code will print "*Good job*". Otherwise it will print "*Wrong answer*".

$n$ can range between $-100$ to $100$ inclusive.

## 🧪 Example

**Input**

```
100
```

**Output**

```
Good job
```

## 💡 Solution

> [!TIP]
> **Key idea:** `Integer.toString(n)` (or `String.valueOf(n)`, or `"" + n`) converts the number to text.

### ✍️ The code you write

```java
String s = Integer.toString(n);
```

### 🔍 How it works

- `DoNotTerminate` is HackerRank's guard against `System.exit`; it uses `SecurityManager`, which newer Java versions disabled, so the local version skips that call.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_int_to_string/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Static Initializer Block](../java_static_initializer_block/README.md) · [☕ All Java exercises](../../../README.md) · [Java Date and Time](../java_date_and_time/README.md) ➡️
