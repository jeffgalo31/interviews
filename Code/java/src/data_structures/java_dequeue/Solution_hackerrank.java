// HackerRank submission copy: paste as-is. Explained version: Solution.java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        Deque<Integer> window = new ArrayDeque<>();
        Map<Integer, Integer> counts = new HashMap<>();
        int best = 0;

        for (int i = 0; i < n; i++) {
            int num = in.nextInt();
            window.addLast(num);
            counts.merge(num, 1, Integer::sum);

            if (window.size() > m) {
                int old = window.removeFirst();
                if (counts.merge(old, -1, Integer::sum) == 0) {
                    counts.remove(old);
                }
            }

            if (window.size() == m) {
                best = Math.max(best, counts.size());
            }
        }
        in.close();
        System.out.println(best);
    }
}
