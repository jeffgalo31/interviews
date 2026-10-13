# Java Comparator

**Type:** HackerRank challenge
**Source:** [Java Comparator](https://www.hackerrank.com/challenges/java-comparator/problem)
**Focus:** Java interfaces, comparator composition, deterministic ordering

## Exercise

Sort players by descending score, then by ascending name when scores tie. The HackerRank editor provides the `Player` type and expects a `Checker` implementing `Comparator<Player>`.

Example input:

```text
4
zoe 100
amy 100
ben 75
lee 100
```

Expected order:

```text
amy 100
lee 100
zoe 100
ben 75
```

## Solution

```java
import java.util.Comparator;

class Checker implements Comparator<Player> {
    @Override
    public int compare(Player left, Player right) {
        int scoreOrder = Integer.compare(right.score, left.score);
        if (scoreOrder != 0) {
            return scoreOrder;
        }
        return left.name.compareTo(right.name);
    }
}
```

The comparator never subtracts scores, so it cannot overflow. Java's `String.compareTo` provides the required ascending lexicographic tie-break.

**Complexity:** One comparison is $O(L)$ in the worst case, where $L$ is the compared name length. Sorting $n$ players takes $O(n \log n)$ comparisons.

**Check:** Scores `100, 100, 75` with names `zoe, amy, ben` sort as `amy 100`, `zoe 100`, `ben 75`.
