// HackerRank submission copy: Java Reflection - Attributes (Easy · Advanced).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.lang.reflect.*;
import java.util.*;

// HackerRank appends the Student class to this code before running it.

public class Solution {

        public static void main(String[] args){
            // ---- your code ----
            Class student = Student.class;
            Method[] methods = student.getDeclaredMethods();
            // ---- end of your code ----

            ArrayList<String> methodList = new ArrayList<>();
            // ---- your code ----
            for(Method method : methods){
                methodList.add(method.getName());
            // ---- end of your code ----
            }
            Collections.sort(methodList);
            for(String name: methodList){
                System.out.println(name);
            }
        }

    }
