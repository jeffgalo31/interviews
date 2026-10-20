package dequeue; // VS Code needs this (folder src/dequeue). HackerRank copy: Solution_hackerrank.java

import java.io.*;
import java.util.*;

/*
 * Java Dequeue - max unique numbers in any contiguous subarray of size M.
 * Full description + step-by-step table in README.md (same folder).
 *
 * HOW INPUT WORKS
 * HackerRank sends the test into STDIN, e.g.:
 *     6 3
 *     5 3 5 2 3 2
 * First line is the SETUP, not data: N = how many numbers follow, M = window size.
 * Second line: the N numbers. We print ONE number: the most unique values found
 * in any window of M numbers in a row.
 *
 * In VS Code nobody sends input when you press Run, so this file falls back to the
 * sample input below. To try your own input, from the java folder:
 *     printf '5 2\n1 1 1 1 1\n' | java src/dequeue/Solution.java      (prints 1)
 */
public class Solution {

    // Same input HackerRank sends in its sample test.
    private static final String SAMPLE_INPUT = "6 3\n5 3 5 2 3 2\n";

    public static void main(String[] args) throws IOException {
        // System.in = STDIN. Scanner lets us read it one number at a time.
        // available() > 0  -> input was piped in: read it (what HackerRank does).
        // otherwise        -> nothing sent: read the SAMPLE_INPUT string instead.
        // (The HackerRank copy just uses new Scanner(System.in).)
        Scanner in = System.in.available() > 0
                ? new Scanner(System.in)
                : new Scanner(SAMPLE_INPUT);

        // nextInt() reads the next number, whether it's on the same line or the next.
        int n = in.nextInt();   // total numbers, e.g. 6  (setup, not part of the array)
        int m = in.nextInt();   // window size,   e.g. 3  (setup, not part of the array)

        // The numbers currently inside the window: oldest at the FRONT, newest at the BACK.
        // A Deque can add/remove at both ends quickly - exactly what a sliding window needs.
        Deque<Integer> window = new ArrayDeque<>();

        // How many times each number appears in the window, e.g. {5=2, 3=1}.
        // counts.size() = how many UNIQUE numbers are in the window right now.
        Map<Integer, Integer> counts = new HashMap<>();

        int best = 0; // highest unique count seen in any full window

        // Read the N numbers one by one and slide the window over them.
        // Window of 3 over 6 numbers fits 6 - 3 + 1 = 4 times (s1..s4 in the README).
        for (int i = 0; i < n; i++) {
            int num = in.nextInt();

            // 1) New number enters at the back of the window; add 1 to its count.
            //    merge(num, 1, Integer::sum) = "if missing put 1, otherwise add 1".
            window.addLast(num);
            counts.merge(num, 1, Integer::sum);

            // 2) Window too big (M + 1 numbers)? The oldest leaves from the front.
            if (window.size() > m) {
                int old = window.removeFirst();
                // Subtract 1 from its count; if it hits 0 the number is no longer in
                // the window, so remove it from the map (it stops counting as unique).
                if (counts.merge(old, -1, Integer::sum) == 0) {
                    counts.remove(old);
                }
            }

            // 3) Window is exactly M numbers: check if it beats the best so far.
            if (window.size() == m) {
                best = Math.max(best, counts.size());
            }
        }

        in.close();

        // One line of output: the answer.
        System.out.println(best);
    }
}
