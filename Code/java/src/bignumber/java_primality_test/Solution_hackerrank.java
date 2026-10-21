// HackerRank submission copy: Java Primality Test (Easy · BigNumber).
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

        String n = bufferedReader.readLine();

        // ---- your code ----
        boolean prime = new BigInteger(n.trim()).isProbablePrime(100);
        System.out.println(prime ? "prime" : "not prime");
        // ---- end of your code ----

        bufferedReader.close();
    }
}
