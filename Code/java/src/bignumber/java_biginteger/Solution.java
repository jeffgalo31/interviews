// Java BigInteger  (Easy · BigNumber)  https://www.hackerrank.com/challenges/java-biginteger/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/bignumber/java_biginteger/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/bignumber/java_biginteger/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - BigInteger has no + or *: use the methods add and multiply.
// - Scanner.nextBigInteger() reads a number of any size.
package bignumber.java_biginteger;

import java.math.BigInteger;
import java.util.Scanner;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "1234\n20\n";
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
        Scanner sc = new Scanner(System.in);
        BigInteger a = sc.nextBigInteger();
        BigInteger b = sc.nextBigInteger();
        sc.close();

        System.out.println(a.add(b));        // a + b
        System.out.println(a.multiply(b));   // a * b
        // ---- end of your code ----
    }
}