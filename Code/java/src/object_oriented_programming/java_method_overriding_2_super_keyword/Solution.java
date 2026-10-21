// Java Method Overriding 2 (Super Keyword)  (Easy · Object Oriented Programming)  https://www.hackerrank.com/challenges/java-method-overriding-2-super-keyword/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/object_oriented_programming/java_method_overriding_2_super_keyword/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - Inside a subclass, define_me() calls the subclass's own (overridden) version.
// - super.define_me() calls the superclass (BiCycle) version instead.
package object_oriented_programming.java_method_overriding_2_super_keyword;

import java.util.*;
import java.io.*;
class Solution{
	public static void main(String []args){
		MotorCycle M=new MotorCycle();
	}
}


class BiCycle{
	String define_me(){
		return "a vehicle with pedals.";
	}
}

class MotorCycle extends BiCycle{
	String define_me(){
		return "a cycle with an engine.";
	}

	MotorCycle(){
		System.out.println("Hello I am a motorcycle, I am "+ define_me());
		String temp=super.define_me(); // super. calls BiCycle's version
		System.out.println("My ancestor is a cycle who is "+ temp );
	}

}