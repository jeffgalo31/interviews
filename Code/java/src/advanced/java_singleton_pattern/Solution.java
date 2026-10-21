// Java Singleton Pattern  (Easy · Advanced)  https://www.hackerrank.com/challenges/java-singleton/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/java_singleton_pattern/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/advanced/java_singleton_pattern/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - A private constructor stops other classes from creating instances.
// - A static field holds the single instance; getSingleInstance() always returns that same object.
// - HackerRank's hidden Solution reads a line, stores it in str and prints the greeting; the local version includes an equivalent main.
package advanced.java_singleton_pattern;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;
// ---- local only: HackerRank's hidden checker does the equivalent of this ----
class Solution {
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "hello world\n";
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
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        Singleton s = Singleton.getSingleInstance();
        s.str = input;
        System.out.println("Hello I am a singleton! Let me say " + Singleton.getSingleInstance().str + " to you");
        sc.close();
    }
}

class Singleton{
    private static final Singleton INSTANCE = new Singleton();   // the one and only instance

    public String str;

    private Singleton() { }                  // private: nobody else can call new Singleton()

    public static Singleton getSingleInstance() {
        return INSTANCE;
    }
}