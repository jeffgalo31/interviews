// HackerRank submission copy: Java String Reverse (Easy · Strings).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        // ---- your code ----
        String reversed = new StringBuilder(A).reverse().toString();
        System.out.println(A.equals(reversed) ? "Yes" : "No");
        // ---- end of your code ----
    }
}
