// HackerRank submission copy: Java 2D Array (Easy · Data Structures).
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
