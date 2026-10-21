// Java Hashset  (Easy · Data Structures)  https://www.hackerrank.com/challenges/java-hashset/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_hashset/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_hashset/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - A HashSet ignores duplicates, so its size is the number of unique pairs so far.
// - Join each pair into one string with a separator; order matters, so (a, b) and (b, a) stay different.
package data_structures.java_hashset;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5\njohn tom\njohn mary\njohn tom\nmary anna\nmary anna\n";
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
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];

        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }
// ---- your code ----
        Set<String> pairs = new HashSet<>();
        for (int i = 0; i < t; i++) {
            pairs.add(pair_left[i] + " " + pair_right[i]);   // the space keeps ("ab","c") != ("a","bc")
            System.out.println(pairs.size());
        }
// ---- end of your code ----
   }
}