<!-- study-layout -->
# Java SHA-256

🟡 **Medium** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/sha-256/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Examples](#-examples) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Cryptographic hash functions are mathematical operations run on digital data; by comparing the computed *hash* (i.e., the output produced by executing a hashing algorithm) to a known and expected hash value, a person can determine the data's integrity. For example, computing the hash of a downloaded file and comparing the result to a previously published hash result can show whether the download has been modified or tampered with. In addition, cryptographic hash functions are extremely collision-resistant; in other words, it should be extremely difficult to produce the same hash output from two different input values using a cryptographic hash function.

*Secure Hash Algorithm 2* (*SHA-2*) is a set of cryptographic hash functions designed by the National Security Agency (NSA). It consists of six identical hashing algorithms (i.e., *SHA-256*, *SHA-512*, *SHA-224*, *SHA-384*, *SHA-512/224*, *SHA-512/256*) with a variable digest size. *SHA-256* is a $256$-bit ($32$ byte) hashing algorithm which can calculate a hash code for an input of up to $264-1$ bits. It undergoes $64$ rounds of hashing and calculates a hash code that is a $64$-digit hexadecimal number.

Given a string, $s$, print its *SHA-256* hash value.

## 📥 Input & output

### Input format

A single alphanumeric string denoting $s$.

### Constraints

- $6 \le |s| \le 20$
- String $s$ consists of English alphabetic letters (i.e., $[a-zA-Z]$ and/or decimal digits (i.e., $0$ through $9$) only.

### Output format

Print the *SHA-256* encryption value of $s$ on a new line.

## 🧪 Examples

### Example 1

**Input**

	HelloWorld

**Output**

	872e4e50ce9990d8b041330c47c9ddd11bec6b503ae9386a99da8584e9bb12c4

### Example 2

**Input**

    Javarmi123

**Output**

	f1d5f8d75bb55c777207c251d07d9091dc10fe7d6682db869106aacb4b7df678

## 💡 Solution

> [!TIP]
> **Key idea:** Same as MD5 with `"SHA-256"`: the digest is 32 bytes, printed as 64 hex digits.

### ✍️ The code you write

```java
Scanner scan = new Scanner(System.in);
String s = scan.next();
scan.close();

byte[] digest = MessageDigest.getInstance("SHA-256").digest(s.getBytes("UTF-8"));

StringBuilder hex = new StringBuilder();
for (byte b : digest) {
    hex.append(String.format("%02x", b));     // 32 bytes -> 64 hex digits
}
System.out.println(hex);
```

### 🔍 How it works

- `%02x` keeps the leading zero of small bytes, so the length is always 64.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/java_sha_256/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java MD5](../java_md5/README.md) · [☕ All Java exercises](../../../README.md)
