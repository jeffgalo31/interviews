// Java Primality Test  (Easy · BigNumber)  https://www.hackerrank.com/challenges/java-primality-test/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/bignumber/java_primality_test/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/bignumber/java_primality_test/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - BigInteger handles numbers far bigger than long (up to 100 digits here).
// - isProbablePrime(certainty): with certainty 100 the chance of a wrong "prime" is below 1 in 2^100.
package bignumber.java_primality_test;

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
    private static final String SAMPLE_INPUT = "13\n";
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
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String n = bufferedReader.readLine();

        // ---- your code ----
        boolean prime = new BigInteger(n.trim()).isProbablePrime(100);
        System.out.println(prime ? "prime" : "not prime");
        // ---- end of your code ----

        bufferedReader.close();
    }
}