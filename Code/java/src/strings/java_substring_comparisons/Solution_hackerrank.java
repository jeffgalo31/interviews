// HackerRank submission copy: Java Substring Comparisons (Easy · Strings).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.Scanner;

public class Solution {
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
