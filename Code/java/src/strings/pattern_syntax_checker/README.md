<!-- study-layout -->
# Pattern Syntax Checker

🟢 **Easy** · 📁 **Strings** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/pattern-syntax-checker/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Using __Regex__, we can easily match or search for patterns in a text. Before searching for a pattern, we have to specify one using some well-defined syntax.

In this problem, you are given a pattern. You have to check whether the syntax of the given pattern is valid.

**Note**: In this problem, a regex is only valid if you can compile it using the  [Pattern.compile](http://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html#compile%28java.lang.String%29) method.

## 📥 Input & output

### Input format

The first line of input contains an integer $N$, denoting the number of test cases. The next $N$ lines contain a string of any printable characters representing the pattern of a regex.

### Output format

For each test case, print ``Valid`` if the syntax of the given pattern is correct. Otherwise, print ``Invalid``. Do not print the quotes.

## 🧪 Example

**Input**

```
3
([A-Z])(.+)
[AZ[a-z](a-z)
batcatpat(nat
```

**Output**

```
Valid
Invalid
Invalid
```

## 💡 Solution

> [!TIP]
> **Key idea:** The definition of valid is "`Pattern.compile` accepts it", so just try to compile.

### ✍️ The code you write

```java
try {
	Pattern.compile(pattern);
	System.out.println("Valid");
} catch (PatternSyntaxException e) {
	System.out.println("Invalid");
}
testCases--;
```

### 🔍 How it works

- A bad pattern throws `PatternSyntaxException`; catch it and print `Invalid`.
- Don't forget `testCases--`, or the loop never ends.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/strings/pattern_syntax_checker/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java String Tokens](../java_string_tokens/README.md) · [☕ All Java exercises](../../../README.md) · [Java Regex](../java_regex/README.md) ➡️
