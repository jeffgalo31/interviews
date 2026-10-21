<!-- study-layout -->
# Valid Username Regular Expression

🟢 **Easy** · 📁 **Strings** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/valid-username-checker/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are updating the username policy on your company's internal networking platform. According to the policy, a username is considered valid if all the following constraints are satisfied:

- The username consists of $8$ to $30$ characters inclusive. If the username consists of less than $8$ or greater than $30$ characters, then it is an invalid username.
- The username can only contain alphanumeric characters and underscores (`_`). Alphanumeric characters describe the character set consisting of *lowercase* characters $[a-z]$, *uppercase* characters $[A-Z]$, and digits $[0-9]$.
- The *first* character of the username must be an *alphabetic* character, i.e., either *lowercase* character $[a-z]$ or *uppercase* character $[A-Z]$.

For example:

| Username | Validity
|:-------:|:---:|
| $\color{red}\texttt{Julia}$| INVALID; Username length < 8 characters  |
|  $\color{green}\texttt{Samantha}$  | VALID |
| $\color{green}\texttt{Samantha_21}$     | VALID |
| $\color{red}\texttt{1}\color{black}\texttt{Samantha}$| INVALID; Username begins with non-alphabetic character |
| $\color{black}\texttt{Samantha}\color{red}\texttt{?}\color{black}\texttt{10_2A}$ | INVALID; '?' character not allowed  |

Update the value of *regularExpression* field in the *UsernameValidator* class so that the regular expression only matches with valid usernames.

## 📥 Input & output

### Input format

The first line of input contains an integer $n$, describing the total number of usernames. Each of the next $n$ lines contains a string describing the username. The locked stub code reads the inputs and validates the username.

### Constraints

- $1 \le n \le 100$
- The username consists of any printable characters.

### Output format

For each of the usernames, the locked stub code prints `Valid` if the username is valid; otherwise `Invalid` each on a new line.

## 🧪 Example

**Input**

```
8
Julia
Samantha
Samantha_21
1Samantha
Samantha?10_2A
JuliaZ007
Julia@007
_Julia007
```

**Output**

```
Invalid
Valid
Valid
Invalid
Invalid
Valid
Invalid
Invalid
```

**Why**

Refer diagram in the challenge statement.

## 💡 Solution

> [!TIP]
> **Key idea:** `[A-Za-z]`: the first character must be a letter.

### ✍️ The code you write

```java
class UsernameValidator {
    // First char a letter, then 7 to 29 letters/digits/underscores: 8 to 30 characters in total.
    public static final String regularExpression = "^[A-Za-z]\\w{7,29}$";
}
```

### 🔍 How it works

- `\w{7,29}`: then 7 to 29 more letters, digits or underscores (`\w`), so the total length is 8 to 30.
- `matches()` must match the whole string; `^` and `$` make that explicit.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/strings/valid_username_regular_expression/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Regex 2 - Duplicate Words](../java_regex_2_duplicate_words/README.md) · [☕ All Java exercises](../../../README.md) · [Tag Content Extractor](../tag_content_extractor/README.md) ➡️
