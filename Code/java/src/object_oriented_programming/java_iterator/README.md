# Java Iterator

**Difficulty:** Easy · **Section:** Object Oriented Programming · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-iterator/problem)

---

Java Iterator class can help you to iterate through every element in a collection. Here is a simple example:

```java
import java.util.*;
public class Example{

    public static void main(String []args){
        ArrayList mylist = new ArrayList();
        mylist.add("Hello");
        mylist.add("Java");
        mylist.add("4");
        Iterator it = mylist.iterator();
        while(it.hasNext()){
            Object element = it.next();
            System.out.println((String)element);
        }
    }
}
```

In this problem you need to complete a method *func*. The method takes an *ArrayList* as input. In that *ArrayList* there is one or more integer numbers, then there is a special string "###", after that there are one or more other strings. A sample *ArrayList* may look like this:

    element[0]=>42
    element[1]=>10
    element[2]=>"###"
    element[3]=>"Hello"
    element[4]=>"Java"

You have to modify the *func* method by editing `at most 2 lines` so that the code only prints the elements after the special string "###". For the sample above the output will be:

    Hello
    Java

*Note:* The stdin doesn't contain the string *"###"*, it is added in the *main* method.

To restore the original code in the editor, click the top left icon on the editor and create a new buffer.

## Solution

The part you write:

```java
Object element = it.next();
if(element instanceof String)//Hints: use instanceof operator
```

- `it.next()` returns the next element and moves the iterator forward.
- The numbers come first; the first `String` is `###`. Stop (`break`) right after reading it.
- The iterator is returned already positioned after `###`, so `main` prints only the strings that follow.
- HackerRank shows no sample input here; the runnable file uses a made-up one: `2 2` (counts), `42 10` (numbers), `Hello Java` (strings).

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/object_oriented_programming/java_iterator/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
