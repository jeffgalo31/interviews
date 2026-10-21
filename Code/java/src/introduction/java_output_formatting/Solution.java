// Java Output Formatting  (Easy · Introduction)  https://www.hackerrank.com/challenges/java-output-formatting/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/introduction/java_output_formatting/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/introduction/java_output_formatting/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - %-15s: the string, left-justified (-) in a field 15 characters wide.
// - %03d: the integer in 3 digits, padded with leading zeros (0).
// - %n: a new line.
package introduction.java_output_formatting;

import java.util.Scanner;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "java 100\ncpp 65\npython 50\n";
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
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                String s1=sc.next();
                int x=sc.nextInt();
                // ---- your code ----
                System.out.printf("%-15s%03d%n", s1, x);
                // ---- end of your code ----
            }
            System.out.println("================================");

    }
}