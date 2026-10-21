// Java String Tokens  (Easy · Strings)  https://www.hackerrank.com/challenges/java-string-tokens/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/strings/java_string_tokens/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/strings/java_string_tokens/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - A token is a run of letters, so split on runs of anything else: [^A-Za-z]+.
// - split gives an empty first element when the string *starts* with a separator, so strip those first.
// - Edge case: a string with no letters at all prints 0.
package strings.java_string_tokens;

import java.io.*;
import java.util.*;
// ---- your code ----
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "He is a very very good boy, isn't he?\n";
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
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();

        // Drop separators at the start, otherwise split() returns an empty first token.
        s = s.replaceFirst("^[^A-Za-z]+", "");

        if (s.isEmpty()) {
            System.out.println(0);
        } else {
            String[] tokens = s.split("[^A-Za-z]+");   // split on every run of non-letters
            System.out.println(tokens.length);
            for (String token : tokens) {
                System.out.println(token);
            }
        }
        scan.close();
    }
}
// ---- end of your code ----
