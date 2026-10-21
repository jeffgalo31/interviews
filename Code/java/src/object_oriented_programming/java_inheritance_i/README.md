# Java Inheritance I

**Difficulty:** Easy · **Section:** Object Oriented Programming · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-inheritance-1/problem)

---

Using *inheritance*, one class can acquire the properties of others. Consider the following *Animal* class:

```java
class Animal{
    void walk(){
        System.out.println("I am walking");
    }
}
```

This class has only one method, *walk*. Next, we want to create a *Bird* class that also has a *fly* method. We do this using *extends* keyword:

```java
class Bird extends Animal {
    void fly() {
        System.out.println("I am flying");
    }
}
```

Finally, we can create a Bird object that can both *fly* and *walk*.

```java
public class Solution{
   public static void main(String[] args){

      Bird bird = new Bird();
      bird.walk();
      bird.fly();
   }
}
```

The above code will print:

    I am walking
    I am flying

This means that a Bird object has all the properties that an Animal object has, as well as some additional unique properties.

The code above is provided for you in your editor. You must add a *sing* method to the *Bird* class, then modify the *main* method accordingly so that the code prints the following lines:

    I am walking
    I am flying
    I am singing

## Solution

The part you write:

```java
void sing()
{
	System.out.println("I am singing");
}
```

- `Bird extends Animal`, so a Bird can `walk()` without declaring it.
- Add `sing()` to `Bird`; `main` already calls it.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/object_oriented_programming/java_inheritance_i/Solution.java` from the `java` folder.
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
