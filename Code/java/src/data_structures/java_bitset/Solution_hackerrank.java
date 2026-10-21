// HackerRank submission copy: Java BitSet (Easy · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();

        BitSet[] sets = { null, new BitSet(n), new BitSet(n) };   // sets[1] = B1, sets[2] = B2

        for (int i = 0; i < m; i++) {
            String op = scan.next();
            int x = scan.nextInt();
            int y = scan.nextInt();

            switch (op) {
                case "AND":  sets[x].and(sets[y]); break;   // result replaces the first operand
                case "OR":   sets[x].or(sets[y]);  break;
                case "XOR":  sets[x].xor(sets[y]); break;
                case "FLIP": sets[x].flip(y);      break;   // here y is a bit index
                case "SET":  sets[x].set(y);       break;
            }
            System.out.println(sets[1].cardinality() + " " + sets[2].cardinality());
        }
        scan.close();
        // ---- end of your code ----
    }
}
