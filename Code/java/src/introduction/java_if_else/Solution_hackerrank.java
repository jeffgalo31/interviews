// HackerRank submission copy: Java If-Else (Easy · Introduction).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        // ---- your code ----
        // Odd, or even between 6 and 20 -> Weird. Every other even number -> Not Weird.
        if (N % 2 != 0 || (N >= 6 && N <= 20)) {
            System.out.println("Weird");
        } else {
            System.out.println("Not Weird");
        }
        // ---- end of your code ----

        scanner.close();
    }
}
