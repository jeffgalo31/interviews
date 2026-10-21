// Java Subarray  (Easy · Data Structures)  https://www.hackerrank.com/challenges/java-negative-subarray/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_subarray/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_subarray/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Every subarray is a pair (start, end) with start ≤ end.
// - For each start, extend end one step at a time and keep a running sum (no need to re-add from scratch).
// - n ≤ 100, so checking all ~5,000 subarrays is instant.
package data_structures.java_subarray;

import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5\n1 -2 4 -5 1\n";
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
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = scan.nextInt();
        scan.close();

        int negatives = 0;
        for (int start = 0; start < n; start++) {
            int sum = 0;
            for (int end = start; end < n; end++) {   // extend the subarray one element at a time
                sum += a[end];
                if (sum < 0) negatives++;
            }
        }
        System.out.println(negatives);
        // ---- end of your code ----
    }
}