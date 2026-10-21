# Java String Tokens

**Difficulty:** Easy · **Section:** Strings · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-string-tokens/problem)

---

Given a string, $s$, matching the regular expression `[A-Za-z !,?._'@]+`, split the string into *tokens*. We define a token to be one or more consecutive English alphabetic letters. Then, print the number of tokens, followed by each token on a new line.

**Note:** You may find the [String.split](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#split-java.lang.String-) method helpful in completing this challenge.

**Input Format**

A single string, $s$.

**Constraints**

- $1 \le \text{ length of } s \le 4 \cdot 10^5$
- $s$ is composed of *any* of the following: English alphabetic letters, blank spaces, exclamation points (`!`), commas (`,`), question marks (`?`), periods (`.`), underscores (`_`), apostrophes (`'`), and at symbols (`@`).

**Output Format**

On the first line, print an integer, $n$, denoting the number of tokens in string $s$ (they *do not* need to be unique). Next, print each of the $n$ tokens on a new line in the same order as they appear in input string $s$.

**Sample Input**

```
He is a very very good boy, isn't he?
```

**Sample Output**

```
10
He
is
a
very
very
good
boy
isn
t
he
```

**Explanation**

We consider a token to be a contiguous segment of alphabetic characters. There are a total of 10 such tokens in string s, and each token is printed in the same order in which it appears in string s.

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

The part you write:

```java
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();

        // Drop separators at the start, otherwise split() returns an empty first token.
        s = s.replaceFirst("^[^A-Za-z]+", "");

        if (s.isEmpty()) {
            System.out.println(0);
        } else {
            String[] tokens = s.split("[^A-Za-z]+");   // split on every run of non-letters
            System.out.println(tokens.length);
            for (String token : tokens) {
                System.out.println(token);
            }
        }
        scan.close();
    }
}
```

- A token is a run of letters, so split on runs of anything else: `[^A-Za-z]+`.
- `split` gives an empty first element when the string *starts* with a separator, so strip those first.
- Edge case: a string with no letters at all prints `0`.

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/strings/java_string_tokens/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
