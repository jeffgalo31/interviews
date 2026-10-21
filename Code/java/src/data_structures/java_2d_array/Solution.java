// Java 2D Array  (Easy · Data Structures)  https://www.hackerrank.com/challenges/java-2d-array/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_2d_array/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_2d_array/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - An hourglass fits with its top-left corner at rows 0..3 and columns 0..3: 16 hourglasses.
// - Sum its 7 cells: 3 on top, 1 in the middle, 3 at the bottom.
// - Start best at Integer.MIN_VALUE: all sums can be negative.
package data_structures.java_2d_array;

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
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "1 1 1 0 0 0\n0 1 0 0 0 0\n1 1 1 0 0 0\n0 0 2 4 4 0\n0 0 0 2 0 0\n0 0 1 2 4 0\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        IntStream.range(0, 6).forEach(i -> {
            try {
                arr.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();

        // ---- your code ----
        int best = Integer.MIN_VALUE;          // values can be negative, so don't start at 0
        for (int r = 0; r <= 3; r++) {         // top-left corner of each hourglass
            for (int c = 0; c <= 3; c++) {
                int sum = arr.get(r).get(c) + arr.get(r).get(c + 1) + arr.get(r).get(c + 2)
                        + arr.get(r + 1).get(c + 1)
                        + arr.get(r + 2).get(c) + arr.get(r + 2).get(c + 1) + arr.get(r + 2).get(c + 2);
                best = Math.max(best, sum);
            }
        }
        System.out.println(best);
        // ---- end of your code ----
    }
}