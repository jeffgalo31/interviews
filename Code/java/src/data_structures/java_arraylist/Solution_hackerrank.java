// HackerRank submission copy: Java Arraylist (Easy · Data Structures).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        // ---- your code ----
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        List<List<Integer>> lines = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int d = scan.nextInt();
            List<Integer> line = new ArrayList<>();
            for (int j = 0; j < d; j++) line.add(scan.nextInt());
            lines.add(line);
        }

        int q = scan.nextInt();
        for (int i = 0; i < q; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            List<Integer> line = lines.get(x - 1);          // positions are 1-based
            if (y >= 1 && y <= line.size()) {
                System.out.println(line.get(y - 1));
            } else {
                System.out.println("ERROR!");
            }
        }
        scan.close();
        // ---- end of your code ----
    }
}
