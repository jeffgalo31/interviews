// HackerRank submission copy: Java Inheritance I (Easy · Object Oriented Programming).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Animal{
	void walk()
	{
		System.out.println("I am walking");
	}
}

class Bird extends Animal
{
	void fly()
	{
		System.out.println("I am flying");
	}
	// ---- your code ----
	void sing()
	{
		System.out.println("I am singing");
	}
	// ---- end of your code ----
}
public class Solution{

   public static void main(String args[]){

	  Bird bird = new Bird();
	  bird.walk();
	  bird.fly();
      bird.sing();

   }
}
