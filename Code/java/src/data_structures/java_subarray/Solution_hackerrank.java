// HackerRank submission copy: Java Subarray (Easy · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = scan.nextInt();
        scan.close();

        int negatives = 0;
        for (int start = 0; start < n; start++) {
            int sum = 0;
            for (int end = start; end < n; end++) {   // extend the subarray one element at a time
                sum += a[end];
                if (sum < 0) negatives++;
            }
        }
        System.out.println(negatives);
        // ---- end of your code ----
    }
}
