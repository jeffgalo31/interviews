# Java Instanceof keyword

**Difficulty:** Easy · **Section:** Object Oriented Programming · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-instanceof-keyword/problem)

---

The Java *instanceof* operator is used to test if the object or instance is an instanceof the specified type.

In this problem we have given you three classes in the editor:

* Student class
* Rockstar class
* Hacker class

In the main method, we populated an *ArrayList* with several instances of these classes. *count* method calculates how many instances of each type is present in the ArrayList. The code prints three integers, the number of instance of Student class, the number of instance of Rockstar class, the number of instance of Hacker class.

But some lines of the code are missing, and you have to fix it by modifying only $3$ lines! Don't add, delete or modify any extra line.

To restore the original code in the editor, click on the top left icon in the editor and create a new buffer.

**Sample Input**

    5
    Student
    Student
    Rockstar
    Student
    Hacker

**Sample Output**

    3 1 1

## Solution

The part you write:

```java
if(element instanceof Student)
   a++;
if(element instanceof Rockstar)
   b++;
if(element instanceof Hacker)
   c++;
```

- `x instanceof Type` is true when the object is that class (or a subclass of it).
- Only the three `if` conditions change (the challenge allows editing exactly 3 lines).

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/object_oriented_programming/java_instanceof_keyword/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
