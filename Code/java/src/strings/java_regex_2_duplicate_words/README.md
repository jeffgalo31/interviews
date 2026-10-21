<!-- study-layout -->
# Java Regex 2 - Duplicate Words

🟡 **Medium** · 📁 **Strings** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/duplicate-word/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

In this challenge, we use regular expressions (RegEx) to remove instances of words that are repeated more than once, but retain the *first occurrence* of any case-insensitive repeated word. For example, the words `love` and `to` are repeated in the sentence `I love Love to To tO code`. Can you complete the code in the editor so it will turn `I love Love to To tO code` into `I love to code`?

To solve this challenge, complete the following three lines:

1. Write a RegEx that will match any repeated word.
2. Complete the second *compile* argument so that the compiled RegEx is case-insensitive.
3. Write the two necessary arguments for *replaceAll* such that each repeated word is replaced with the very first instance the word found in the sentence. It must be the *exact* first occurrence of the word, as the expected output is case-sensitive.

**Note:** This challenge uses a custom checker; you will fail the challenge if you modify anything other than the three locations that the comments direct you to complete. To restore the editor's original stub code, create a new buffer by clicking on the branch icon in the top left of the editor.

## 📥 Input & output

### Input format

The following input is handled for you the given stub code:

The first line contains an integer, $n$, denoting the number of sentences.
Each of the $n$ subsequent lines contains a single sentence consisting of English alphabetic letters and whitespace characters.

### Constraints

- Each sentence consists of *at most* $10^4$ English alphabetic letters and whitespaces.
- $1\le n \le 100$

### Output format

Stub code in the editor prints the sentence modified by the *replaceAll* line to stdout. The modified string must be a modified version of the initial sentence where all repeat occurrences of each word are removed.

## 🧪 Example

**Input**

```
5
Goodbye bye bye world world world
Sam went went to to to his business
Reya is is the the best player in eye eye game
in inthe
Hello hello Ab aB
```

**Output**

```
Goodbye bye world
Sam went to his business
Reya is the best player in eye game
in inthe
Hello Ab
```

**Why**

- We remove the second occurrence of `bye` and the second and third occurrences of `world` from `Goodbye bye bye world world world` to get `Goodbye bye world`.
- We remove the second occurrence of `went` and the second and third occurrences of `to` from `Sam went went to to to his business` to get `Sam went to his business`.
- We remove the second occurrence of `is`, the second occurrence of `the`, and the second occurrence of `eye` from `Reya is is the the best player in eye eye game` to get `Reya is the best player in eye game`.
- The sentence `in inthe` has no repeated words, so we do not modify it.
- We remove the second occurrence of `ab` from `Hello hello Ab aB` to get `Hello Ab`. It's important to note that our matching is case-insensitive, and we specifically retained the first occurrence of the matched word in our final string.

## 💡 Solution

> [!TIP]
> **Key idea:** `\b(\w+)` captures a whole word; `(?:\W+\1\b)+` matches one or more repeats of that **same** word (`\1`) after separators.

### ✍️ The code you write

```java
String regex = "\\b(\\w+)(?:\\W+\\1\\b)+";
Pattern p = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
    // ...
input = input.replaceAll(m.group(), m.group(1));
```

### 🔍 How it works

- `Pattern.CASE_INSENSITIVE` makes `bye` and `Bye` count as the same word.
- Replace the whole matched run (`m.group()`) with its first word (`m.group(1)`), which keeps the original capitalization.
- Regex backslashes are doubled inside Java strings.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/strings/java_regex_2_duplicate_words/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Regex](../java_regex/README.md) · [☕ All Java exercises](../../../README.md) · [Valid Username Regular Expression](../valid_username_regular_expression/README.md) ➡️
