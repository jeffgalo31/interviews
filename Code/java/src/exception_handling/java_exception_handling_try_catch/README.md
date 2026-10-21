# Java Exception Handling (Try-catch)

**Difficulty:** Easy · **Section:** Exception Handling · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-exception-handling-try-catch/problem)

---

Exception handling is the process of responding to the occurrence, during computation, of exceptions – anomalous or exceptional conditions requiring special processing – often changing the normal flow of program execution. (Wikipedia)
***

Java has built-in mechanism to handle exceptions. Using the *try* statement we can test a block of code for errors. The *catch* block contains the code that says what to do if exception occurs.

This problem will test your knowledge on try-catch block.

You will be given two integers $x$ and $y$ as input, you have to compute $x/y$. If $x$ and $y$ are not $32$ bit signed integers or if $y$ is zero, exception will occur and you have to report it. Read sample Input/Output to know what to report in case of exceptions.

**Sample Input 0:**

	10
    3

**Sample Output 0:**

	3

**Sample Input 1:**

	10
    Hello

**Sample Output 1:**

	java.util.InputMismatchException

**Sample Input 2:**

	10
    0

**Sample Output 2:**

	java.lang.ArithmeticException: / by zero

**Sample Input 3:**

	23.323
    0

**Sample Output 3:**

	java.util.InputMismatchException

## Solution

The part you write:

```java
Scanner scan = new Scanner(System.in);
try {
    int x = scan.nextInt();
    int y = scan.nextInt();
    System.out.println(x / y);
} catch (InputMismatchException e) {
    // Not a 32-bit integer (text, decimal, too big): print just the exception's class name.
    System.out.println(e.getClass().getName());
} catch (ArithmeticException e) {
    // Division by zero: print the exception including its message ("/ by zero").
    System.out.println(e);
}
scan.close();
```

- `nextInt()` throws `InputMismatchException` when the next token isn't a 32-bit integer ("Hello", "23.323").
- Integer division by zero throws `ArithmeticException: / by zero`.
- Printing an exception (`println(e)`) shows `class name: message`; for the mismatch case HackerRank expects only the class name, so print `getClass().getName()`.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/exception_handling/java_exception_handling_try_catch/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
