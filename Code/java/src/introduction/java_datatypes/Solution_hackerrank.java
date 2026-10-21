// HackerRank submission copy: Java Datatypes (Easy · Introduction).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.*;
import java.io.*;



class Solution{
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
