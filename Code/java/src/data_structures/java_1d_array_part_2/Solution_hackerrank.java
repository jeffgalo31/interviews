// HackerRank submission copy: Java 1D Array (Part 2) (Medium · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;

public class Solution {
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
