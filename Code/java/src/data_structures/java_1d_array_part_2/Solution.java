// Java 1D Array (Part 2)  (Medium · Data Structures)  https://www.hackerrank.com/challenges/java-1d-array/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_1d_array_part_2/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_1d_array_part_2/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - A depth-first search over the three moves: jump i + leap, step forward i + 1, step back i - 1.
// - Reaching any index ≥ n means you left the array: win.
// - Mark each visited cell as 1 so moving back and forth can't loop forever (each cell is visited at most once).
package data_structures.java_1d_array_part_2;

import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "4\n5 3\n0 0 0 0 0\n6 5\n0 0 0 1 1 1\n6 3\n0 0 1 1 1 0\n3 1\n0 1 0\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    // ---- your code ----
    public static boolean canWin(int leap, int[] game) {
        return canWinFrom(0, leap, game);
    }

    private static boolean canWinFrom(int i, int leap, int[] game) {
        if (i >= game.length) return true;                 // walked or jumped off the end: win
        if (i < 0 || game[i] == 1) return false;            // outside on the left, or a 1 (blocked/visited)

        game[i] = 1;                                         // mark visited so we never loop back here
        return canWinFrom(i + leap, leap, game)
            || canWinFrom(i + 1, leap, game)
            || canWinFrom(i - 1, leap, game);
    }
    // ---- end of your code ----

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();

            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}