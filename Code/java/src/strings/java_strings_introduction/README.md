<!-- study-layout -->
# Java Strings Introduction

🟢 **Easy** · 📁 **Strings** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-strings-introduction/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

> "A string is traditionally a sequence of characters, either as a literal constant or as some kind of variable." &mdash; [Wikipedia: String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))

This exercise is to test your understanding of Java Strings. A sample *String* declaration:

    String myString = "Hello World!"

The elements of a *String* are called *characters*. The number of *characters* in a *String* is called the *length*, and it can be retrieved with the *String.length()* method.

Given two strings of lowercase English letters, $A$ and $B$, perform the following operations:

1. Sum the lengths of $A$ and $B$.
2. Determine if $A$ is lexicographically larger than $B$ (i.e.: does $B$ come before $A$ in the dictionary?).
3. Capitalize the first letter in $A$ and $B$ and print them on a single line, separated by a space.

## 📥 Input & output

### Input format

The first line contains a string $A$.
The second line contains another string $B$.
The strings are comprised of only lowercase English letters.

### Output format

There are three lines of output:
For the first line, sum the lengths of $A$ and $B$.
For the second line, write `Yes` if $A$ is lexicographically greater than $B$ otherwise print `No` instead.
For the third line, capitalize the first letter in both $A$ and $B$ and print them on a single line, separated by a space.

## 🧪 Example

**Input**

```
hello
java
```

**Output**

```
9
No
Hello Java
```

**Why**

String A is "hello" and B is "java".

A has a length of 5, and B has a length of 4; the sum of their lengths is 9. When sorted alphabetically/lexicographically, "hello" precedes "java"; therefore, A is not greater than B and the answer is `No`.

When you capitalize the first letter of both A and B and then print them separated by a space, you get "Hello Java".

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** `length()` gives the number of characters.

### ✍️ The code you write

```java
System.out.println(A.length() + B.length());
System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
System.out.println(capitalize(A) + " " + capitalize(B));
    // ...
static String capitalize(String s) {
    return s.substring(0, 1).toUpperCase() + s.substring(1);
}
```

### 🔍 How it works

- `A.compareTo(B) > 0` means A comes after B in dictionary order.
- Capitalize: first letter `substring(0, 1).toUpperCase()` + the rest `substring(1)`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/strings/java_strings_introduction/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Currency Formatter](../../introduction/java_currency_formatter/README.md) · [☕ All Java exercises](../../../README.md) · [Java Substring](../java_substring/README.md) ➡️
