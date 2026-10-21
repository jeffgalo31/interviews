// HackerRank submission copy: Java List (Easy · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) list.add(scan.nextInt());

        int q = scan.nextInt();
        for (int i = 0; i < q; i++) {
            String query = scan.next();
            if (query.equals("Insert")) {
                int x = scan.nextInt();
                int y = scan.nextInt();
                list.add(x, y);              // insert y at index x (shifts the rest right)
            } else {                         // "Delete"
                int x = scan.nextInt();
                list.remove(x);              // int argument -> removes by INDEX
            }
        }
        scan.close();

        StringBuilder out = new StringBuilder();
        for (int value : list) out.append(value).append(' ');
        System.out.println(out.toString().trim());
        // ---- end of your code ----
    }
}
