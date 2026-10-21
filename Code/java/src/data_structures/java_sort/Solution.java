// Java Sort  (Easy · Data Structures)  https://www.hackerrank.com/challenges/java-sort/problem
// Description and explanation: README.md (same folder).
//
// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run
//   java src/data_structures/java_sort/Solution.java
// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).
// Your own input:  printf '...' | java src/data_structures/java_sort/Solution.java
// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;
//   the part you write is between the "your code" markers).
//
// Locally the class with main() comes first (so this single file can run);
// HackerRank's order and the exact part you write are in Solution_hackerrank.java.
//
// How it works:
// - Build the comparator from three keys: comparingDouble(getCgpa).reversed(), then thenComparing(getFname), then thenComparingInt(getId).
// - reversed() applies to the CGPA key only, because it is called before adding the other keys.
package data_structures.java_sort;

import java.util.*;
//Complete the code
public class Solution
{
    // ---- local only: with no piped input, use HackerRank's sample input ----
    private static final String SAMPLE_INPUT = "5\n33 Rumpa 3.68\n85 Ashis 3.85\n56 Samiha 3.75\n19 Samara 3.75\n22 Fahim 3.76\n";
    static {
        try {
            if (System.in.available() == 0) {
                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));
            }
        } catch (java.io.IOException e) {
            // keep reading the real input
        }
    }

	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());

		List<Student> studentList = new ArrayList<Student>();
		while(testCases>0){
			int id = in.nextInt();
			String fname = in.next();
			double cgpa = in.nextDouble();

			Student st = new Student(id, fname, cgpa);
			studentList.add(st);

			testCases--;
		}
		studentList.sort(Comparator.comparingDouble(Student::getCgpa).reversed()   // CGPA high -> low
				.thenComparing(Student::getFname)                                 // then name A -> Z
				.thenComparingInt(Student::getId));                               // then id

      	for(Student st: studentList){
			System.out.println(st.getFname());
		}
	}
}

class Student{
	private int id;
	private String fname;
	private double cgpa;
	public Student(int id, String fname, double cgpa) {
		super();
		this.id = id;
		this.fname = fname;
		this.cgpa = cgpa;
	}
	public int getId() {
		return id;
	}
	public String getFname() {
		return fname;
	}
	public double getCgpa() {
		return cgpa;
	}
}