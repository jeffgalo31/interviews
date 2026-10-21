<!-- study-layout -->
# Java Map

🟢 **Easy** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/phone-book/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are given a phone book that consists of people's names and their phone number. After that you will be given some person's name as query. For each query, print the phone number of that person.

## 📥 Input & output

### Input format

The first line will have an integer $n$ denoting the number of entries in the phone book. Each entry consists of two lines: a name and the corresponding phone number. <br>

After these, there will be some queries. Each query will contain a person's name. Read the queries until end-of-file.

*Constraints:*<br>
A person's name consists of only lower-case English letters and it may be in the format 'first-name last-name' or in the format 'first-name'. Each phone number has exactly 8 digits without any leading zeros.<br>

$1 \le n \le 100000$<br>
$1 \le Query \le 100000$<br>

### Output format

For each case, print "Not found" if the person has no entry in the phone book. Otherwise, print the person's name and phone number. See sample output for the exact format.

To make the problem easier, we provided a portion of the code in the editor. You can either complete that code or write completely on your own.

## 🧪 Example

**Input**

```
3
uncle sam
99912222
tom
11122222
harry
12299933
uncle sam
uncle tom
harry
```

**Output**

```
uncle sam=99912222
Not found
harry=12299933
```

## 💡 Solution

> [!TIP]
> **Key idea:** A `HashMap` stores name → phone and finds a name in constant time (up to 100,000 queries).

### ✍️ The code you write

```java
Map<String, Integer> phoneBook = new HashMap<>();
    // ...
phoneBook.put(name, phone);
    // ...
if (phoneBook.containsKey(s)) {
	System.out.println(s + "=" + phoneBook.get(s));
} else {
	System.out.println("Not found");
}
```

### 🔍 How it works

- `containsKey` tells whether the person is in the book.
- Names can have a space ("uncle sam"), so read whole lines with `nextLine()`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_map/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java List](../java_list/README.md) · [☕ All Java exercises](../../../README.md) · [Java Stack](../java_stack/README.md) ➡️
