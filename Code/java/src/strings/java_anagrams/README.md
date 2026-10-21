<!-- study-layout -->
# Java Anagrams

🟢 **Easy** · 📁 **Strings** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-anagrams/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Examples](#-examples) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Two strings, $a$ and $b$, are called anagrams if they contain all the same characters in the same frequencies.  For this challenge, the test is not case-sensitive. For example, the anagrams of `CAT` are `CAT`, `ACT`, `tac`, `TCA`, `aTC`, and `CtA`.

### Function Description

Complete the *isAnagram* function in the editor.

*isAnagram* has the following parameters:

- *string a:* the first string
- *string b:* the second string

### Returns

- *boolean:* If $a$ and $b$ are case-insensitive anagrams, return true.  Otherwise, return false.

## 📥 Input & output

### Input format

The first line contains a string $a$.
The second line contains a string $b$.

### Constraints

- $1 \le length(a), length(b) \le 50$
- Strings $a$ and $b$ consist of English alphabetic characters.
- The comparison should NOT be case sensitive.

## 🧪 Examples

### Example 1

**Input**

```
anagram
margana
```

**Output**

```
Anagrams
```

**Why**

| Character | Frequency: `anagram` | Frequency: `margana` |
| --- | --- | --- |
| `A` or `a` | 3 | 3 |
| `G` or `g` | 1 | 1 |
| `N` or `n` | 1 | 1 |
| `M` or `m` | 1 | 1 |
| `R` or `r` | 1 | 1 |

The two strings contain all the same letters in the same frequencies, so we print "Anagrams".

### Example 2

**Input**

```
anagramm
marganaa
```

**Output**

```
Not Anagrams
```

**Why**

| Character | Frequency: `anagramm` | Frequency: `marganaa` |
| --- | --- | --- |
| `A` or `a` | 3 | 4 |
| `G` or `g` | 1 | 1 |
| `N` or `n` | 1 | 1 |
| `M` or `m` | 2 | 1 |
| `R` or `r` | 1 | 1 |

The two strings don't contain the same number of `a`'s and `m`'s, so we print "Not Anagrams".

### Example 3

**Input**

```
Hello
hello
```

**Output**

```
Anagrams
```

**Why**

| Character | Frequency: `Hello` | Frequency: `hello` |
| --- | --- | --- |
| `E` or `e` | 1 | 1 |
| `H` or `h` | 1 | 1 |
| `L` or `l` | 2 | 2 |
| `O` or `o` | 1 | 1 |

The two strings contain all the same letters in the same frequencies, so we print "Anagrams".

## 💡 Solution

> [!TIP]
> **Key idea:** Lowercase both strings so the check is not case-sensitive.

### ✍️ The code you write

```java
static boolean isAnagram(String a, String b) {
    if (a.length() != b.length()) return false;

    int[] counts = new int[26];                 // one counter per letter a..z
    for (char c : a.toLowerCase().toCharArray()) counts[c - 'a']++;
    for (char c : b.toLowerCase().toCharArray()) counts[c - 'a']--;

    for (int count : counts) {
        if (count != 0) return false;           // some letter appears a different number of times
    }
    return true;
}
```

### 🔍 How it works

- Count letters: +1 for each letter of `a`, −1 for each letter of `b`. Anagrams end with every counter at 0.
- `c - 'a'` turns a letter into an index 0..25. (HackerRank's challenge asks not to use `java.util` sorting.)

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/strings/java_anagrams/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java String Reverse](../java_string_reverse/README.md) · [☕ All Java exercises](../../../README.md) · [Java String Tokens](../java_string_tokens/README.md) ➡️
