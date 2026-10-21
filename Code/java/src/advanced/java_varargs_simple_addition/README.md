# Java Varargs - Simple Addition

**Difficulty:** Easy · **Section:** Advanced · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/simple-addition-varargs/problem)

---

You are given a class *Solution* and its *main* method in the editor. <br>Your task is to create the class *Add* and the required methods so that the code prints the *sum of the numbers* passed to the function *add*.

**Note:** Your *add* method in the *Add* class must print the *sum* as given in the *Sample Output*

**Input Format**

There are six lines of input, each containing an integer.

**Output Format**

There will be only four lines of output. Each line contains the sum of the *integers* passed as the parameters to *add* in the *main* method.

**Sample Input**

```
1
2
3
4
5
6
```

**Sample Output**

```
1+2=3
1+2+3=6
1+2+3+4+5=15
1+2+3+4+5+6=21
```

## Solution

The part you write:

```java
class Add {
    void add(int... numbers) {               // varargs: any number of ints, received as an int[]
        StringBuilder expression = new StringBuilder();
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (i > 0) expression.append('+');
            expression.append(numbers[i]);
            sum += numbers[i];
        }
        System.out.println(expression + "=" + sum);
    }
}
```

- `int... numbers` (varargs) accepts 2, 3, 5 or 6 arguments with a **single** method; inside, `numbers` is an `int[]`.
- The locked code rejects overloading, so one varargs method is the only way.
- Print `1+2=3`: numbers joined by `+`, then `=` and the sum.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/advanced/java_varargs_simple_addition/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
