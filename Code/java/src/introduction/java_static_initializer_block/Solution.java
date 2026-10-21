// Java Static Initializer Block  (Easy · Introduction)  https://www.hackerrank.com/challenges/java-static-initializer-block/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/introduction/java_static_initializer_block/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/introduction/java_static_initializer_block/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - A static { ... } block runs once when the class is loaded, before main.
// - It reads B and H into static fields and sets flag; the locked main only prints the area when flag is true.
// - The exact error text is printed (not thrown) so the output matches.
package introduction.java_static_initializer_block;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "1\n3\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

// ---- your code ----
    static int B, H;
    static boolean flag = true;

    // Runs once, when the class is loaded, before main().
    static {
        Scanner sc = new Scanner(System.in);
        B = sc.nextInt();
        H = sc.nextInt();
        sc.close();
        if (B <= 0 || H <= 0) {
            flag = false;
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
    }
// ---- end of your code ----
public static void main(String[] args) {
		if(flag)
		{
			int area=B*H;
			System.out.print(area);
		}

	}//end of main

}//end of class
