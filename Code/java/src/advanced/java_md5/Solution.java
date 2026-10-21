// Java MD5  (Medium · Advanced)  https://www.hackerrank.com/challenges/java-md5/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/java_md5/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/advanced/java_md5/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - MessageDigest.getInstance("MD5") gives the hash function; digest(bytes) returns 16 bytes.
// - Print each byte as two hex digits with %02x (the 0 keeps leading zeros like 0f).
package advanced.java_md5;

import java.math.BigInteger;
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

        byte[] digest = MessageDigest.getInstance("MD5").digest(s.getBytes("UTF-8"));

        StringBuilder hex = new StringBuilder();
        for (byte b : digest) {
            hex.append(String.format("%02x", b));     // each byte as 2 lowercase hex digits
        }
        System.out.println(hex);
        // ---- end of your code ----
    }
}