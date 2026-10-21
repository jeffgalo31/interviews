// Java SHA-256  (Medium · Advanced)  https://www.hackerrank.com/challenges/sha-256/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/java_sha_256/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/advanced/java_sha_256/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Same as MD5 with "SHA-256": the digest is 32 bytes, printed as 64 hex digits.
// - %02x keeps the leading zero of small bytes, so the length is always 64.
package advanced.java_sha_256;

import java.security.MessageDigest;
import java.util.Scanner;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "HelloWorld\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


    public static void main(String[] args) throws Exception {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        scan.close();

        byte[] digest = MessageDigest.getInstance("SHA-256").digest(s.getBytes("UTF-8"));

        StringBuilder hex = new StringBuilder();
        for (byte b : digest) {
            hex.append(String.format("%02x", b));     // 32 bytes -> 64 hex digits
        }
        System.out.println(hex);
        // ---- end of your code ----
    }
}