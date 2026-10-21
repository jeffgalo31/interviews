// Java Lambda Expressions  (Medium · Advanced)  https://www.hackerrank.com/challenges/java-lambda-expressions/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/java_lambda_expressions/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/advanced/java_lambda_expressions/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - PerformOperation has exactly one method, so a lambda a -> ... can implement it.
// - One-line lambdas return their expression; multi-line lambdas use { ... return ...; }.
// - HackerRank's code starts MyMath but leaves it open: the closing } is part of the code you write.
package advanced.java_lambda_expressions;

import java.io.*;
import java.util.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5\n1 4\n2 5\n3 898\n1 3\n2 12\n";
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
  MyMath ob = new MyMath();
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  int T = Integer.parseInt(br.readLine());
  PerformOperation op;
  boolean ret = false;
  String ans = null;
  while (T--> 0) {
   String s = br.readLine().trim();
   StringTokenizer st = new StringTokenizer(s);
   int ch = Integer.parseInt(st.nextToken());
   int num = Integer.parseInt(st.nextToken());
   if (ch == 1) {
    op = ob.isOdd();
    ret = ob.checker(op, num);
    ans = (ret) ? "ODD" : "EVEN";
   } else if (ch == 2) {
    op = ob.isPrime();
    ret = ob.checker(op, num);
    ans = (ret) ? "PRIME" : "COMPOSITE";
   } else if (ch == 3) {
    op = ob.isPalindrome();
    ret = ob.checker(op, num);
    ans = (ret) ? "PALINDROME" : "NOT PALINDROME";

   }
   System.out.println(ans);
  }
 }
}
interface PerformOperation {
 boolean check(int a);
}
class MyMath {
 public static boolean checker(PerformOperation p, int num) {
  return p.check(num);
 }
   public PerformOperation isOdd() {
       return a -> a % 2 != 0;
   }

   public PerformOperation isPrime() {
       return a -> {
           if (a < 2) return false;
           for (int d = 2; (long) d * d <= a; d++) {
               if (a % d == 0) return false;
           }
           return true;
       };
   }

   public PerformOperation isPalindrome() {
       return a -> {
           String s = Integer.toString(a);
           return new StringBuilder(s).reverse().toString().equals(s);
       };
   }
}