<!-- study-layout -->
# Prime Checker

🟡 **Medium** · 📁 **Advanced** · ☕ HackerRank Java · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/prime-checker/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are given a class *Solution* and its *main* method in the editor. Your task is to create a class *Prime*. The class *Prime* should contain a single method *checkPrime*.

The locked code in the editor will call the *checkPrime* method with one or more integer arguments. You should write the *checkPrime* method in such a way that the code prints only the [prime numbers](https://en.wikipedia.org/wiki/Prime_number).

Please read the code given in the editor carefully. Also please do not use method overloading!

### Note

You may get a compile time error in this problem due to the statement below:

      BufferedReader br=new BufferedReader(new InputStreamReader(in));

This was added intentionally, and you have to figure out a way to get rid of the error.

## 📥 Input & output

### Input format

There are only five lines of input, each containing one integer.

### Output format

There will be only four lines of output. Each line contains only prime numbers depending upon the parameters passed to *checkPrime* in the *main* method of the class *Solution*. In case there is no prime number, then a blank line should be printed.

## 🧪 Example

**Input**

```
2
1
3
4
5
```

**Output**

```
2
2
2 3
2 3 5
```

## 💡 Solution

> [!TIP]
> **Key idea:** The locked code uses `in` without `System.`: `import static java.lang.System.in;` fixes that compile error.

### ✍️ The code you write

```java
import static java.lang.System.in;   // makes the bare `in` in main mean System.in (the "compile error" to fix)

class Prime {
    void checkPrime(int... numbers) {        // one varargs method: no overloading allowed
        StringBuilder line = new StringBuilder();
        for (int n : numbers) {
            if (isPrime(n)) line.append(n).append(' ');
        }
        System.out.println(line);
    }

    private static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int d = 2; (long) d * d <= n; d++) {
            if (n % d == 0) return false;
        }
        return true;
    }
}
```

### 🔍 How it works

- `checkPrime(int... numbers)` (varargs) handles 1, 2, 3 or 5 arguments with one method.
- Print the primes separated by spaces (a blank line when there are none). Trial division up to √n is enough.
- HackerRank's locked code refers to `misc.Prime`; the local version uses `Prime`, because the class isn't in a `misc` package here.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java src/advanced/prime_checker/Solution.java` |
| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |

---

⬅️ [Can You Access?](../can_you_access/README.md) · [☕ All Java exercises](../../../README.md) · [Java Factory Pattern](../java_factory_pattern/README.md) ➡️
