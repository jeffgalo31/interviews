<!-- study-layout -->
# Java Stack

🟡 **Medium** · 📁 **Data Structures** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/java-stack/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

In computer science, a stack or LIFO (last in, first out) is an abstract data type that serves as a collection of elements, with two principal operations: push, which adds an element to the collection, and pop, which removes the last element that was added.(Wikipedia)

A string containing only parentheses is balanced if the following is true:
1. if it is an empty string
2. if A and B are correct, AB is correct,
3. if A is correct, (A) and {A} and [A] are also correct.

Examples of some correctly balanced strings are: "{}()",  "[{()}]",  "({()})" <br>

Examples of some unbalanced strings are: "{}(",  "({)}",  "[[",  "}{" etc.<br>

Given a string, determine if it is balanced or not.

## 📥 Input & output

### Input format

There will be multiple lines in the input file, each having a single non-empty string. You should read input till end-of-file.

The part of the code that handles input operation is already provided in the editor.

### Output format

For each case, print 'true' if the string is balanced, 'false' otherwise.

## 🧪 Example

**Input**

```
{}()
({()})
{}(
[]
```

**Output**

```
true
true
false
true
```

## 💡 Solution

> [!TIP]
> **Key idea:** Push every opening bracket on a stack; a closing bracket must match the **most recent** opener (pop).

### ✍️ The code you write

```java
System.out.println(isBalanced(input));
    // ...
static boolean isBalanced(String s) {
	Deque<Character> stack = new ArrayDeque<>();
	for (char c : s.toCharArray()) {
		if (c == '(' || c == '[' || c == '{') {
			stack.push(c);                              // remember every opener
		} else {
			if (stack.isEmpty()) return false;          // a closer with nothing open
			char open = stack.pop();                    // must close the most recent opener
			if ((c == ')' && open != '(') || (c == ']' && open != '[') || (c == '}' && open != '{')) {
				return false;
			}
		}
	}
	return stack.isEmpty();                             // anything left open -> unbalanced
}
```

### 🔍 How it works

- Fail on a closer when the stack is empty, or when the pair doesn't match.
- At the end the stack must be empty (nothing left open).
- `ArrayDeque` is the recommended stack in Java (the old `Stack` class is slower).

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/data_structures/java_stack/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Java Map](../java_map/README.md) · [☕ All Java exercises](../../../README.md) · [Java Hashset](../java_hashset/README.md) ➡️
