<!-- study-layout -->
# Java MD5

🟡 **Medium** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-md5/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Examples](#-examples) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

*MD5* (*Message-Digest algorithm 5*) is a widely-used cryptographic hash function with a $128$-bit hash value. Here are some common uses for *MD5*:

* To store a one-way hash of a password.
* To provide some assurance that a transferred file has arrived intact.

*MD5* is one in a series of message digest algorithms designed by Professor Ronald Rivest of MIT (Rivest, $1994$); however, the security of *MD5* has been severely compromised, most infamously by the Flame malware in $2012$. The *CMU Software Engineering Institute* essentially considers *MD5* to be ["cryptographically broken and unsuitable for further use"](https://en.wikipedia.org/wiki/MD5).

Given an alphanumeric string, $s$, denoting a password, compute and print its *MD5* encryption value.

## 📥 Input & output

### Input format

A single alphanumeric string denoting $s$.

### Constraints

* $ 6 \le |s| \le 20 $
- String $s$ consists of English alphabetic letters (i.e., $[a-zA-Z]$ and/or decimal digits (i.e., $0$ through $9$) only.

### Output format

Print the *MD5* encryption value of $s$ on a new line.

## 🧪 Examples

### Example 1

**Input**

	HelloWorld

**Output**

	68e109f0f40ca72a15e05cc22786f8e6

### Example 2

**Input**

    Javarmi123

**Output**

	2da2d1e0ce7b4951a858ed2d547ef485

## 💡 Solution

> [!TIP]
> **Key idea:** `MessageDigest.getInstance("MD5")` gives the hash function; `digest(bytes)` returns 16 bytes.

### ✍️ The code you write

```java
Scanner scan = new Scanner(System.in);
String s = scan.next();
scan.close();

byte[] digest = MessageDigest.getInstance("MD5").digest(s.getBytes("UTF-8"));

StringBuilder hex = new StringBuilder();
for (byte b : digest) {
    hex.append(String.format("%02x", b));     // each byte as 2 lowercase hex digits
}
System.out.println(hex);
```

### 🔍 How it works

- Print each byte as two hex digits with `%02x` (the `0` keeps leading zeros like `0f`).

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/java_md5/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Lambda Expressions](../java_lambda_expressions/README.md) · [☕ All Java exercises](../../../README.md) · [Java SHA-256](../java_sha_256/README.md) ➡️
