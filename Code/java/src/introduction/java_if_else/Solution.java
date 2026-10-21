// Java If-Else  (Easy · Introduction)  https://www.hackerrank.com/challenges/java-if-else/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/introduction/java_if_else/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/introduction/java_if_else/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - N % 2 != 0 means N is odd (the remainder of dividing by 2 is not 0).
// - The four rules collapse into one test: Weird if odd *or* between 6 and 20; otherwise Not Weird.
package introduction.java_if_else;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "3\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        // ---- your code ----
        // Odd, or even between 6 and 20 -> Weird. Every other even number -> Not Weird.
        if (N % 2 != 0 || (N >= 6 && N <= 20)) {
            System.out.println("Weird");
        } else {
            System.out.println("Not Weird");
        }
        // ---- end of your code ----

        scanner.close();
    }
}