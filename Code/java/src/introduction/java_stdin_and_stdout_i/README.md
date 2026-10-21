<!-- study-layout -->
# Java Stdin and Stdout I

🟢 **Easy** · 📁 **Introduction** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Most HackerRank challenges require you to read input from [stdin](https://en.wikipedia.org/wiki/Standard_streams#Standard_input_.28stdin.29) (standard input) and write output to [stdout](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29) (standard output).

One popular way to read input from stdin is by using the [Scanner class](https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html) and specifying the *Input Stream* as *System.in*. For example:

```java
Scanner scanner = new Scanner(System.in);
String myString = scanner.next();
int myInt = scanner.nextInt();
scanner.close();

System.out.println("myString is: " + myString);
System.out.println("myInt is: " + myInt);
```

The code above creates a *Scanner* object named $scanner$ and uses it to read a *String* and an *int*. It then *closes* the *Scanner* object because there is no more input to read, and prints to stdout using *System.out.println(String)*. So, if our input is:

	Hi 5

Our code will print:

	myString is: Hi
    myInt is: 5

Alternatively, you can use the [BufferedReader class](https://docs.oracle.com/javase/8/docs/api/java/io/BufferedReader.html).

### Task

In this challenge, you must read $3$ integers from stdin and then print them to stdout. Each integer must be printed on a new line. To make the problem a little easier, a portion of the code is provided for you in the editor below.

## 📥 Input & output

### Input format

There are $3$ lines of input, and each line contains a single integer.

## 🧪 Example

**Input**

```
42
100
125
```

**Output**

```
42
100
125
```

## 💡 Solution

> [!TIP]
> **Key idea:** `nextInt()` reads the next integer, whatever line it is on.

### ✍️ The code you write

```java
int b = scan.nextInt();
int c = scan.nextInt();
    // ...
System.out.println(b);
System.out.println(c);
```

### 🔍 How it works

- Read all three first, then print each one with `println` (one per line).

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/introduction/java_stdin_and_stdout_i/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Welcome to Java!](../welcome_to_java/README.md) · [☕ All Java exercises](../../../README.md) · [Java If-Else](../java_if_else/README.md) ➡️
