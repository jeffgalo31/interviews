// HackerRank submission copy: Java Static Initializer Block (Easy · Introduction).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
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
