// Java Inheritance I  (Easy · Object Oriented Programming)  https://www.hackerrank.com/challenges/java-inheritance-1/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/object_oriented_programming/java_inheritance_i/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - Bird extends Animal, so a Bird can walk() without declaring it.
// - Add sing() to Bird; main already calls it.
package object_oriented_programming.java_inheritance_i;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
public class Solution{

   public static void main(String args[]){

	  Bird bird = new Bird();
	  bird.walk();
	  bird.fly();
      bird.sing();

   }
}

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
	void sing()
	{
		System.out.println("I am singing");
	}
}