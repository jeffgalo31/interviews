<!-- study-layout -->
# Java End-of-file

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-end-of-file/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

> "In computing, *End Of File* (commonly abbreviated *EOF*) is a condition in a computer operating system where no more data can be read from a data source."
&mdash; <cite>([Wikipedia: End-of-file](https://en.wikipedia.org/wiki/End-of-file))</cite>

The challenge here is to read $n$ lines of input until you reach *EOF*, then number and print all $n$ lines of content.

**Hint:** Java's *Scanner.hasNext()* method is helpful for this problem.

## 📥 Input & output

### Input format

Read some unknown $n$ lines of input from *stdin(System.in)* until you reach *EOF*; each line of input contains a non-empty *String*.

### Output format

For each line, print the line number, followed by a single space, and then the line content received as input.

## 🧪 Example

**Input**

```
Hello world
I am a file
Read me until end-of-file.
```

**Output**

```
1 Hello world
2 I am a file
3 Read me until end-of-file.
```

## 💡 Solution

> [!TIP]
> **Key idea:** `hasNextLine()` becomes false at end-of-file, so the loop needs no line count.

### ✍️ The code you write

```java
Scanner sc = new Scanner(System.in);
int lineNumber = 1;
while (sc.hasNextLine()) {                 // false once the input ends (EOF)
    System.out.println(lineNumber + " " + sc.nextLine());
    lineNumber++;
}
sc.close();
```

### 🔍 How it works

- Keep a counter and print it in front of each line.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_end_of_file/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Datatypes](../java_datatypes/README.md) · [☕ All Java exercises](../../../README.md) · [Java Static Initializer Block](../java_static_initializer_block/README.md) ➡️
