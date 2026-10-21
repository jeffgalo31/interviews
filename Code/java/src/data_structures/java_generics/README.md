# Java Generics

**Difficulty:** Easy · **Section:** Data Structures · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-generics/problem)

---

Generic methods are a very efficient way to handle multiple datatypes using a single method. This problem will test your knowledge on Java Generic methods.

Let's say you have an integer array and a string array. You have to write a **single** method *printArray* that can print all the elements of both arrays. The method should be able to accept both integer arrays or string arrays.

You are given code in the editor. Complete the code so that it prints the following lines:

    1
    2
    3
    Hello
    World

Do not use method overloading because your answer will not be accepted.

## Solution

The part you write:

```java
class Printer
{
   <T> void printArray(T[] array) {          // T can be Integer, String, ... one method for all
       for (T element : array) {
           System.out.println(element);
       }
   }
}
```

- `<T>` before the return type makes a **generic method**: one `printArray` that works for `Integer[]`, `String[]`, ...
- The locked code counts methods named `printArray`; a generic method keeps it at one (no overloading).

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/data_structures/java_generics/Solution.java` from the `java` folder.
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
