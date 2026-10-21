// Java 1D Array  (Easy · Data Structures)  https://www.hackerrank.com/challenges/java-1d-array-introduction/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_1d_array/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_1d_array/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - new int[n] creates an array with room for n integers (all start at 0).
// - Store the i-th value at index i, then print the array in order.
// - HackerRank's newer template for this challenge reads the numbers from one line; this version uses Scanner, which reads them whether they are on one line or several.
package data_structures.java_1d_array;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5\n10\n20\n30\n40\n50\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    public static void main(String[] args) throws IOException {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        int[] a = new int[n];                 // 1. an array that holds n integers
        for (int i = 0; i < n; i++) {
            int val = scan.nextInt();
            a[i] = val;                       // 2. save each value at its own index
        }
        scan.close();

        for (int i = 0; i < a.length; i++) {  // print each element on its own line
            System.out.println(a[i]);
        }
        // ---- end of your code ----
    }
}