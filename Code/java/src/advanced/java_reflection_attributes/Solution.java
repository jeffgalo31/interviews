// Java Reflection - Attributes  (Easy · Advanced)  https://www.hackerrank.com/challenges/java-reflection-attributes/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/advanced/java_reflection_attributes/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// How it works:
// - Student.class is the Class object describing Student.
// - getDeclaredMethods() lists every method declared in the class (any visibility).
// - Collect the names with getName(); the locked code sorts and prints them.
package advanced.java_reflection_attributes;

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

// ---- local only: HackerRank appends this Student class (taken from the challenge's code) ----
class Student{
    private String name;
    private String id;
    private String email;

    public String getName() {
        return name;
    }
    public String getId() {
        return id;
    }
    public String getEmail() {
        return email;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setId(String id) {
        this.id = id;
    }
    public void setEmail(String email) {
        this.email = email;
    }
}