// HackerRank submission copy: paste as-is. Explained version: Solution.java
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNextLine()) {
            String ip = in.nextLine();
            System.out.println(ip.matches(new MyRegex().pattern));
        }
        in.close();
    }
}

class MyRegex {
    private static final String PART = "(25[0-5]|2[0-4]\\d|[01]?\\d?\\d)";
    String pattern = "(" + PART + "\\.){3}" + PART;
}
