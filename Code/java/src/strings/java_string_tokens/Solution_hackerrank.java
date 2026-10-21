// HackerRank submission copy: Java String Tokens (Easy · Strings).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;

// ---- your code ----
public class Solution {

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
