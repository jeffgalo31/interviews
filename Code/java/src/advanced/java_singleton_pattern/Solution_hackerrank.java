// HackerRank submission copy: Java Singleton Pattern (Easy · Advanced).
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
class Singleton{
    private static final Singleton INSTANCE = new Singleton();   // the one and only instance

    public String str;

    private Singleton() { }                  // private: nobody else can call new Singleton()

    public static Singleton getSingleInstance() {
        return INSTANCE;
    }
}
// ---- end of your code ----
