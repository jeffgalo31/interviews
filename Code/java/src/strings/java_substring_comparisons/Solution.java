// Java Substring Comparisons  (Easy · Strings)  https://www.hackerrank.com/challenges/java-string-compare/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/strings/java_substring_comparisons/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/strings/java_substring_comparisons/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Slide a window of length k over the string: s.substring(i, i + k) for every start index.
// - Start both answers with the first window, then keep whichever compares smaller / larger (compareTo).
// - Uppercase letters sort before lowercase (Zoo < ball), which compareTo already does.
package strings.java_substring_comparisons;

import java.util.Scanner;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "welcometojava\n3\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    // ---- your code ----
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);

        // Every substring of length k starts at some index i from 0 to s.length() - k.
        for (int i = 1; i <= s.length() - k; i++) {
            String current = s.substring(i, i + k);
            if (current.compareTo(smallest) < 0) smallest = current;
            if (current.compareTo(largest) > 0) largest = current;
        }

        return smallest + "\n" + largest;
    }
    // ---- end of your code ----

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}