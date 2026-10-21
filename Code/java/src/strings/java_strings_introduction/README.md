# Java Strings Introduction

**Difficulty:** Easy · **Section:** Strings · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-strings-introduction/problem)

---

> "A string is traditionally a sequence of characters, either as a literal constant or as some kind of variable." &mdash; [Wikipedia: String (computer science)](https://en.wikipedia.org/wiki/String_(computer_science))

This exercise is to test your understanding of Java Strings. A sample *String* declaration:

    String myString = "Hello World!"

The elements of a *String* are called *characters*. The number of *characters* in a *String* is called the *length*, and it can be retrieved with the *String.length()* method.

Given two strings of lowercase English letters, $A$ and $B$, perform the following operations:

1. Sum the lengths of $A$ and $B$.
2. Determine if $A$ is lexicographically larger than $B$ (i.e.: does $B$ come before $A$ in the dictionary?).
3. Capitalize the first letter in $A$ and $B$ and print them on a single line, separated by a space.

**Input Format**

The first line contains a string $A$.
The second line contains another string $B$.
The strings are comprised of only lowercase English letters.

**Output Format**

There are three lines of output:
For the first line, sum the lengths of $A$ and $B$.
For the second line, write `Yes` if $A$ is lexicographically greater than $B$ otherwise print `No` instead.
For the third line, capitalize the first letter in both $A$ and $B$ and print them on a single line, separated by a space.

**Sample Input 0**

```
hello
java
```

**Sample Output 0**

```
9
No
Hello Java
```

**Explanation**

String A is "hello" and B is "java".

A has a length of 5, and B has a length of 4; the sum of their lengths is 9. When sorted alphabetically/lexicographically, "hello" precedes "java"; therefore, A is not greater than B and the answer is `No`.

When you capitalize the first letter of both A and B and then print them separated by a space, you get "Hello Java".

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

The part you write:

```java
System.out.println(A.length() + B.length());
System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
System.out.println(capitalize(A) + " " + capitalize(B));
    // ...
static String capitalize(String s) {
    return s.substring(0, 1).toUpperCase() + s.substring(1);
}
```

- `length()` gives the number of characters.
- `A.compareTo(B) > 0` means A comes after B in dictionary order.
- Capitalize: first letter `substring(0, 1).toUpperCase()` + the rest `substring(1)`.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/strings/java_strings_introduction/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
