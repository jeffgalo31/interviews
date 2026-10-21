// Java BigDecimal  (Medium · BigNumber)  https://www.hackerrank.com/challenges/java-bigdecimal/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/bignumber/java_bigdecimal/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/bignumber/java_bigdecimal/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Sort the strings but compare them as BigDecimal numbers, so each number is printed exactly as it was typed.
// - b.compareTo(a) (reversed) gives descending order.
// - Arrays.sort on objects is stable: equal values like 0.12 and .12 keep their input order.
// - Sort only indexes 0..n because the array has 2 extra null slots.
package bignumber.java_bigdecimal;

import java.math.BigDecimal;
import java.util.*;
class Solution{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "9\n-100\n50\n0\n56.6\n90\n0.12\n.12\n02.34\n000.000\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n + 2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
        sc.close();
        // ---- your code ----
        // Sort only the first n entries (the array has 2 extra empty slots).
        // Compare as numbers, largest first; keep the original strings so ".12" stays ".12".
        Arrays.sort(s, 0, n, (a, b) -> new BigDecimal(b).compareTo(new BigDecimal(a)));
        // ---- end of your code ----
        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }
}