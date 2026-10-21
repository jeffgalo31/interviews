// Java Loops II  (Easy · Introduction)  https://www.hackerrank.com/challenges/java-loops/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/introduction/java_loops_ii/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/introduction/java_loops_ii/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Each term is the previous term plus 2^j * b, so keep a running value instead of recomputing the sum.
// - 1 << j is 2 to the power j (shifting the bit 1 left j times).
// - StringBuilder collects the numbers so the line is printed once, with spaces only between them.
package introduction.java_loops_ii;

import java.util.*;
import java.io.*;
class Solution{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "2\n0 2 10\n5 3 5\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            // ---- your code ----
            StringBuilder line = new StringBuilder();
            int value = a;
            for (int j = 0; j < n; j++) {
                value += (1 << j) * b;        // add 2^j * b
                line.append(value);
                if (j < n - 1) line.append(' ');
            }
            System.out.println(line);
            // ---- end of your code ----
        }
        in.close();
    }
}