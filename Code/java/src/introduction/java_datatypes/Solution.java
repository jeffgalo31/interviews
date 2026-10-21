// Java Datatypes  (Easy · Introduction)  https://www.hackerrank.com/challenges/java-datatypes/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/introduction/java_datatypes/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/introduction/java_datatypes/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Ranges: byte −128..127, short −32768..32767, int about ±2.1 billion, long about ±9.2 × 10^18.
// - Short.MIN_VALUE, Integer.MAX_VALUE, ... avoid typing the limits by hand.
// - If nextLong() throws, the number is too big even for a long, and the locked catch prints "can't be fitted anywhere".
package introduction.java_datatypes;

import java.util.*;
import java.io.*;
class Solution{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5\n-150\n150000\n1500000000\n213333333333333333333333333333333333\n-100000000000000\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

    public static void main(String []argh)
    {



        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {

            try
            {
                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x>=-128 && x<=127)System.out.println("* byte");
                // ---- your code ----
                if (x >= Short.MIN_VALUE && x <= Short.MAX_VALUE) System.out.println("* short");
                if (x >= Integer.MIN_VALUE && x <= Integer.MAX_VALUE) System.out.println("* int");
                System.out.println("* long");   // nextLong() succeeded, so it always fits in a long
                // ---- end of your code ----
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        }
    }
}