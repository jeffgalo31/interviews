<!-- study-layout -->
# Java Regex

🟡 **Medium** · 📁 **Strings** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-regex/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Write a class called MyRegex which will contain a string pattern. You need to write a regular expression and assign it to the pattern such that it can be used to validate an IP address. Use the following definition of an IP address:

```
IP address is a string in the form "A.B.C.D", where the value of A, B, C, and D may range from 0 to 255. Leading zeros are allowed. The length of A, B, C, or D can't be greater than 3.
```

Some valid IP address:

```
000.12.12.034
121.234.12.12
23.45.12.56
```

Some invalid IP address:

```
000.12.234.23.23
666.666.23.23
.213.123.23.32
23.45.22.32.
I.Am.not.an.ip
```

In this problem you will be provided strings containing any combination of ASCII characters. You have to write a regular expression to find the valid IPs.

Just write the MyRegex class which contains a String . The string should contain the correct regular expression.

(MyRegex class MUST NOT be public)

## 🧪 Example

**Input**

```
000.12.12.034
121.234.12.12
23.45.12.56
00.12.123.123123.123
122.23
Hello.IP
```

**Output**

```
true
true
true
false
false
false
```

## 💡 Solution

See `Solution.java`. The pattern:

```
((25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(25[0-5]|2[0-4]\d|[01]?\d?\d)
```

One part (0-255, 1-3 digits, leading zeros allowed) is one of three alternatives:

| Alternative  | Matches                   | Examples             |
| ------------ | ------------------------- | -------------------- |
| `25[0-5]`    | 250-255                   | 250, 255             |
| `2[0-4]\d`   | 200-249                   | 200, 234, 249        |
| `[01]?\d?\d` | 0-199, with leading zeros | 0, 12, 034, 000, 199 |

### What `[01]?\d?\d` means, piece by piece

The symbols:

| Symbol | Meaning                                                    |
| ------ | ---------------------------------------------------------- |
| `[01]` | one character that is either `0` or `1`                    |
| `\d`   | one digit, `0`-`9` (always means the same thing)           |
| `?`    | makes the thing **right before it** optional: 0 or 1 times |

The pattern, in order (3 positions):

| Position | Piece   | Meaning                                                |
| -------- | ------- | ------------------------------------------------------ |
| 1st      | `[01]?` | optional: a `0` or `1`                                 |
| 2nd      | `\d?`   | optional: any digit                                    |
| 3rd      | `\d`    | required: any digit (no `?`, so a part is never empty) |

Reading it left to right: _an optional `0` or `1`, then an optional digit, then one required digit._
That allows 1, 2 or 3 digits, and when there are 3 the first one must be `0` or `1`,
so the highest it can go is `199`. Anything from 200 up is handled by the other two alternatives.

| Input | How it matches `[01]?\d?\d`                                                          |
| ----- | ------------------------------------------------------------------------------------ |
| `7`   | `[01]?` skipped, `\d?` skipped, `\d` = 7                                             |
| `45`  | `[01]?` skipped, `\d?` = 4, `\d` = 5                                                 |
| `034` | `[01]?` = 0, `\d?` = 3, `\d` = 4                                                     |
| `199` | `[01]?` = 1, `\d?` = 9, `\d` = 9                                                     |
| `299` | no match: three digits but the first isn't `0`/`1` (and `2[0-4]\d` only goes to 249) |

- `(part\.){3}` = three parts each followed by a dot, then one final `part` with no dot.
- `String.matches()` must match the **whole** string, so no `^`/`$` anchors are needed.
  That's what rejects `23.45.22.32.`, `.213.123.23.32` and five-part addresses.
- In Java source every `\` is doubled: `\d` is written `"\\d"` and `\.` is `"\\."`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/strings/java_regex/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Pattern Syntax Checker](../pattern_syntax_checker/README.md) · [☕ All Java exercises](../../../README.md) · [Java Regex 2 - Duplicate Words](../java_regex_2_duplicate_words/README.md) ➡️
