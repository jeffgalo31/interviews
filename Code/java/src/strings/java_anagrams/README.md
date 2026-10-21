# Java Anagrams

**Difficulty:** Easy · **Section:** Strings · **Track:** HackerRank Java · [Open on HackerRank](https://www.hackerrank.com/challenges/java-anagrams/problem)

---

Two strings, $a$ and $b$, are called anagrams if they contain all the same characters in the same frequencies.  For this challenge, the test is not case-sensitive. For example, the anagrams of `CAT` are `CAT`, `ACT`, `tac`, `TCA`, `aTC`, and `CtA`.

**Function Description**

Complete the *isAnagram* function in the editor.

*isAnagram* has the following parameters:

- *string a:* the first string
- *string b:* the second string

**Returns**

- *boolean:* If $a$ and $b$ are case-insensitive anagrams, return true.  Otherwise, return false.

**Input Format**

The first line contains a string $a$.
The second line contains a string $b$.

**Constraints**

- $1 \le length(a), length(b) \le 50$
- Strings $a$ and $b$ consist of English alphabetic characters.
- The comparison should NOT be case sensitive.

**Sample Input 0**

```
anagram
margana
```

**Sample Output 0**

```
Anagrams
```

**Explanation 0**

| Character | Frequency: `anagram` | Frequency: `margana` |
| --- | --- | --- |
| `A` or `a` | 3 | 3 |
| `G` or `g` | 1 | 1 |
| `N` or `n` | 1 | 1 |
| `M` or `m` | 1 | 1 |
| `R` or `r` | 1 | 1 |

The two strings contain all the same letters in the same frequencies, so we print "Anagrams".

**Sample Input 1**

```
anagramm
marganaa
```

**Sample Output 1**

```
Not Anagrams
```

**Explanation 1**

| Character | Frequency: `anagramm` | Frequency: `marganaa` |
| --- | --- | --- |
| `A` or `a` | 3 | 4 |
| `G` or `g` | 1 | 1 |
| `N` or `n` | 1 | 1 |
| `M` or `m` | 2 | 1 |
| `R` or `r` | 1 | 1 |

The two strings don't contain the same number of `a`'s and `m`'s, so we print "Not Anagrams".

**Sample Input 2**

```
Hello
hello
```

**Sample Output 2**

```
Anagrams
```

**Explanation 2**

| Character | Frequency: `Hello` | Frequency: `hello` |
| --- | --- | --- |
| `E` or `e` | 1 | 1 |
| `H` or `h` | 1 | 1 |
| `L` or `l` | 2 | 2 |
| `O` or `o` | 1 | 1 |

The two strings contain all the same letters in the same frequencies, so we print "Anagrams".

## Solution

The part you write:

```java
static boolean isAnagram(String a, String b) {
    if (a.length() != b.length()) return false;

    int[] counts = new int[26];                 // one counter per letter a..z
    for (char c : a.toLowerCase().toCharArray()) counts[c - 'a']++;
    for (char c : b.toLowerCase().toCharArray()) counts[c - 'a']--;

    for (int count : counts) {
        if (count != 0) return false;           // some letter appears a different number of times
    }
    return true;
}
```

- Lowercase both strings so the check is not case-sensitive.
- Count letters: +1 for each letter of `a`, −1 for each letter of `b`. Anagrams end with every counter at 0.
- `c - 'a'` turns a letter into an index 0..25. (HackerRank's challenge asks not to use `java.util` sorting.)

**Files**

- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `java src/strings/java_anagrams/Solution.java` from the `java` folder (with no input it uses the sample input).
- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.
