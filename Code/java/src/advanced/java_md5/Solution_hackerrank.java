// HackerRank submission copy: Java MD5 (Medium · Advanced).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.math.BigInteger;
import java.security.MessageDigest;
import java.util.Scanner;

public class Solution {

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
