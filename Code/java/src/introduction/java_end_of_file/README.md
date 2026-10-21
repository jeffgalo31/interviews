# Java End-of-file

**Difficulty:** Easy · **Section:** Introduction · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-end-of-file/problem)

---

> "In computing, *End Of File* (commonly abbreviated *EOF*) is a condition in a computer operating system where no more data can be read from a data source."
&mdash; <cite>([Wikipedia: End-of-file](https://en.wikipedia.org/wiki/End-of-file))</cite>

The challenge here is to read $n$ lines of input until you reach *EOF*, then number and print all $n$ lines of content.

**Hint:** Java's *Scanner.hasNext()* method is helpful for this problem.

**Input Format**

Read some unknown $n$ lines of input from *stdin(System.in)* until you reach *EOF*; each line of input contains a non-empty *String*.

**Output Format**

For each line, print the line number, followed by a single space, and then the line content received as input.

**Sample Input**

```
Hello world
I am a file
Read me until end-of-file.
```

**Sample Output**

```
1 Hello world
2 I am a file
3 Read me until end-of-file.
```

## Solution

The part you write:

```java
Scanner sc = new Scanner(System.in);
int lineNumber = 1;
while (sc.hasNextLine()) {                 // false once the input ends (EOF)
    System.out.println(lineNumber + " " + sc.nextLine());
    lineNumber++;
}
sc.close();
```

- `hasNextLine()` becomes false at end-of-file, so the loop needs no line count.
- Keep a counter and print it in front of each line.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/introduction/java_end_of_file/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
