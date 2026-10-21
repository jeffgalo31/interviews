// HackerRank submission copy: Prime Checker (Medium · Advanced).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;
// ---- your code ----
import static java.lang.System.in;   // makes the bare `in` in main mean System.in (the "compile error" to fix)

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
// ---- end of your code ----
public class Solution {

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
		Method[] methods=misc.Prime.class.getDeclaredMethods();
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

}
