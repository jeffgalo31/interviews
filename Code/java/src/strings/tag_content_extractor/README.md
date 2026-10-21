<!-- study-layout -->
# Tag Content Extractor

🟡 **Medium** · 📁 **Strings** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/tag-content-extractor/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

In a tag-based language like *XML* or *HTML*, contents are enclosed between a *start tag* and an *end tag* like `<tag>contents</tag>`. Note that the corresponding *end tag* starts with a `/`.

Given a string of text in a tag-based language, parse this text and retrieve the contents enclosed within sequences of well-organized tags meeting the following criterion:

1. The name of the *start* and *end* tags must be same. The HTML code `<h1>Hello World</h2>` is *not valid*, because the text starts with an `h1` tag and ends with a non-matching `h2` tag.

2. Tags can be nested, but content between nested tags is considered *not valid*. For example, in `<h1><a>contents</a>invalid</h1>`, `contents` is *valid* but `invalid` is *not valid*.

3. Tags can consist of any printable characters.

## 📥 Input & output

### Input format

The first line of input contains a single integer, $N$ (the number of lines).
The $N$ subsequent lines each contain a line of text.

### Constraints

- $1 \leq N \leq 100$
- Each line contains a maximum of $10^4$ printable characters.
- The total number of characters in all test cases will not exceed $10^6$.

### Output format

For each line, print the content enclosed within valid tags.
If a line contains multiple instances of valid content, print out each instance of valid content on a new line; if no valid content is found, print `None`.

## 🧪 Example

**Input**

```
4
<h1>Nayeem loves counseling</h1>
<h1><h1>Sanjay has no watch</h1></h1><par>So wait for a while</par>
<Amee>safat codes like a ninja</amee>
<SA premium>Imtiaz has a secret crush</SA premium>
```

**Output**

```
Nayeem loves counseling
Sanjay has no watch
So wait for a while
None
Imtiaz has a secret crush
```

## 💡 Solution

> [!TIP]
> **Key idea:** `<(.+)>` captures the start tag's name; `</\1>` requires the end tag to have the **same** name.

### ✍️ The code you write

```java
// <tag>content</tag>: same tag name (\1), content without any '<' (so no nested tags).
Matcher m = Pattern.compile("<(.+)>([^<]+)</\\1>").matcher(line);
boolean found = false;
while (m.find()) {
	System.out.println(m.group(2));
	found = true;
}
if (!found) {
	System.out.println("None");
}
```

### 🔍 How it works

- `([^<]+)` is the content: it may not contain `<`, which rejects text that is itself wrapped around other tags.
- Print every match on its own line, or `None` when there are none.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/strings/tag_content_extractor/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Valid Username Regular Expression](../valid_username_regular_expression/README.md) · [☕ All Java exercises](../../../README.md) · [Java BigDecimal](../../bignumber/java_bigdecimal/README.md) ➡️
