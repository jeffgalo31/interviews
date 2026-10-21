// Java BitSet  (Easy · Data Structures)  https://www.hackerrank.com/challenges/java-bitset/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_bitset/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_bitset/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Keep the two sets in an array so 1 and 2 from the input pick the set directly.
// - and / or / xor change the set they're called on (the first operand), as the problem requires.
// - cardinality() is the number of set bits.
package data_structures.java_bitset;

import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5 4\nAND 1 2\nSET 1 4\nFLIP 2 2\nOR 2 1\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


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