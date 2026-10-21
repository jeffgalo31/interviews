// Prime Checker  (Medium · Advanced)  https://www.hackerrank.com/challenges/prime-checker/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/prime_checker/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/advanced/prime_checker/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - The locked code uses in without System.: import static java.lang.System.in; fixes that compile error.
// - checkPrime(int... numbers) (varargs) handles 1, 2, 3 or 5 arguments with one method.
// - Print the primes separated by spaces (a blank line when there are none). Trial division up to √n is enough.
// - HackerRank's locked code refers to misc.Prime; the local version uses Prime, because the class isn't in a misc package here.
package advanced.prime_checker;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;
// ---- your code ----
import static java.lang.System.in;
public class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "2\n1\n3\n4\n5\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }


	public static void main(String[] args) {
		try{
		BufferedReader br=new BufferedReader(new InputStreamReader(in));
		int n1=Integer.parseInt(br.readLine());
		int n2=Integer.parseInt(br.readLine());
		int n3=Integer.parseInt(br.readLine());
		int n4=Integer.parseInt(br.readLine());
		int n5=Integer.parseInt(br.readLine());
		Prime ob=new Prime();
		ob.checkPrime(n1);
		ob.checkPrime(n1,n2);
		ob.checkPrime(n1,n2,n3);
		ob.checkPrime(n1,n2,n3,n4,n5);
		Method[] methods=Prime.class.getDeclaredMethods();
		Set<String> set=new HashSet<>();
		boolean overload=false;
		for(int i=0;i<methods.length;i++)
		{
			if(set.contains(methods[i].getName()))
			{
				overload=true;
				break;
			}
			set.add(methods[i].getName());

		}
		if(overload)
		{
			throw new Exception("Overloading not alloweed");
		}
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	}

}   // makes the bare `in` in main mean System.in (the "compile error" to fix)

class Prime {
    void checkPrime(int... numbers) {        // one varargs method: no overloading allowed
        StringBuilder line = new StringBuilder();
        for (int n : numbers) {
            if (isPrime(n)) line.append(n).append(' ');
        }
        System.out.println(line);
    }

    private static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int d = 2; (long) d * d <= n; d++) {
            if (n % d == 0) return false;
        }
        return true;
    }
}