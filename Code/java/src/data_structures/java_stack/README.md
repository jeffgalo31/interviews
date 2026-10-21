# Java Stack

**Difficulty:** Medium · **Section:** Data Structures · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-stack/problem)

---

In computer science, a stack or LIFO (last in, first out) is an abstract data type that serves as a collection of elements, with two principal operations: push, which adds an element to the collection, and pop, which removes the last element that was added.(Wikipedia)

A string containing only parentheses is balanced if the following is true:
1. if it is an empty string
2. if A and B are correct, AB is correct,
3. if A is correct, (A) and {A} and [A] are also correct.

Examples of some correctly balanced strings are: "{}()",  "[{()}]",  "({()})" <br>

Examples of some unbalanced strings are: "{}(",  "({)}",  "[[",  "}{" etc.<br>

Given a string, determine if it is balanced or not.

**Input Format**

There will be multiple lines in the input file, each having a single non-empty string. You should read input till end-of-file.

The part of the code that handles input operation is already provided in the editor.

**Output Format**

For each case, print 'true' if the string is balanced, 'false' otherwise.

**Sample Input**

```
{}()
({()})
{}(
[]
```

**Sample Output**

```
true
true
false
true
```

## Solution

The part you write:

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

- Push every opening bracket on a stack; a closing bracket must match the **most recent** opener (pop).
- Fail on a closer when the stack is empty, or when the pair doesn't match.
- At the end the stack must be empty (nothing left open).
- `ArrayDeque` is the recommended stack in Java (the old `Stack` class is slower).

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/data_structures/java_stack/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
