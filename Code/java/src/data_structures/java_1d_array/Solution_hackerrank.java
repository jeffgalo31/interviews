// HackerRank submission copy: Java 1D Array (Easy · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
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
    public static void main(String[] args) throws IOException {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        int[] a = new int[n];                 // 1. an array that holds n integers
        for (int i = 0; i < n; i++) {
            int val = scan.nextInt();
            a[i] = val;                       // 2. save each value at its own index
        }
        scan.close();

        for (int i = 0; i < a.length; i++) {  // print each element on its own line
            System.out.println(a[i]);
        }
        // ---- end of your code ----
    }
}
