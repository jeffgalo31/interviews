// Java Arraylist  (Easy · Data Structures)  https://www.hackerrank.com/challenges/java-arraylist/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_arraylist/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_arraylist/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Each line has a different length, so use a list of lists: List<List<Integer>>.
// - Queries use 1-based positions: line x is get(x - 1), position y is get(y - 1).
// - Check y <= size() before reading, otherwise print ERROR!.
package data_structures.java_arraylist;

import java.io.*;
import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5\n5 41 77 74 22 44\n1 12\n4 37 34 36 52\n0\n3 20 22 33\n5\n1 3\n3 4\n3 1\n4 3\n5 5\n";
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

        List<List<Integer>> lines = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int d = scan.nextInt();
            List<Integer> line = new ArrayList<>();
            for (int j = 0; j < d; j++) line.add(scan.nextInt());
            lines.add(line);
        }

        int q = scan.nextInt();
        for (int i = 0; i < q; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            List<Integer> line = lines.get(x - 1);          // positions are 1-based
            if (y >= 1 && y <= line.size()) {
                System.out.println(line.get(y - 1));
            } else {
                System.out.println("ERROR!");
            }
        }
        scan.close();
        // ---- end of your code ----
    }
}