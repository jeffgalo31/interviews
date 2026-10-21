// HackerRank submission copy: Java SHA-256 (Medium · Advanced).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.security.MessageDigest;
import java.util.Scanner;

public class Solution {

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
