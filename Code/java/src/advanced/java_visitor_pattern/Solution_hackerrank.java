// HackerRank submission copy: Java Visitor Pattern (Medium · Advanced).
// Paste the whole file; if HackerRank shows part of the code as locked, paste only the
// lines between "// ---- your code ----" and "// ---- end of your code ----".
// Explained, runnable version: Solution.java
import java.util.ArrayList;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

import java.util.ArrayList;
import java.util.Scanner;

enum Color {
    RED, GREEN
}

abstract class Tree {

    private int value;
    private Color color;
    private int depth;

    public Tree(int value, Color color, int depth) {
        this.value = value;
        this.color = color;
        this.depth = depth;
    }

    public int getValue() {
        return value;
    }

    public Color getColor() {
        return color;
    }

    public int getDepth() {
        return depth;
    }

    public abstract void accept(TreeVis visitor);
}

class TreeNode extends Tree {

    private ArrayList<Tree> children = new ArrayList<>();

    public TreeNode(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitNode(this);

        for (Tree child : children) {
            child.accept(visitor);
        }
    }

    public void addChild(Tree child) {
        children.add(child);
    }
}

class TreeLeaf extends Tree {

    public TreeLeaf(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitLeaf(this);
    }
}

abstract class TreeVis
{
    public abstract int getResult();
    public abstract void visitNode(TreeNode node);
    public abstract void visitLeaf(TreeLeaf leaf);

}
// ---- your code ----
class SumInLeavesVisitor extends TreeVis {
    private int sum = 0;

    public int getResult() {
        return sum;
    }

    public void visitNode(TreeNode node) {
        // inner nodes don't count
    }

    public void visitLeaf(TreeLeaf leaf) {
        sum += leaf.getValue();
    }
}

class ProductOfRedNodesVisitor extends TreeVis {
    private static final long MOD = 1_000_000_007L;
    private long product = 1;                          // product of no values = 1

    public int getResult() {
        return (int) product;
    }

    private void multiplyIfRed(Tree t) {
        if (t.getColor() == Color.RED) {
            product = (product * t.getValue()) % MOD;   // keep it small after every step
        }
    }

    public void visitNode(TreeNode node) {
        multiplyIfRed(node);
    }

    public void visitLeaf(TreeLeaf leaf) {
        multiplyIfRed(leaf);
    }
}

class FancyVisitor extends TreeVis {
    private int evenDepthNodeSum = 0;
    private int greenLeafSum = 0;

    public int getResult() {
        return Math.abs(evenDepthNodeSum - greenLeafSum);
    }

    public void visitNode(TreeNode node) {
        if (node.getDepth() % 2 == 0) evenDepthNodeSum += node.getValue();
    }

    public void visitLeaf(TreeLeaf leaf) {
        if (leaf.getColor() == Color.GREEN) greenLeafSum += leaf.getValue();
    }
}

public class Solution {

    public static Tree solve() {
        //read the tree from STDIN and return its root as a return value of this function
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] values = new int[n + 1];
        Color[] colors = new Color[n + 1];
        for (int i = 1; i <= n; i++) values[i] = scan.nextInt();
        for (int i = 1; i <= n; i++) colors[i] = scan.nextInt() == 0 ? Color.RED : Color.GREEN;

        List<List<Integer>> neighbors = new ArrayList<>();
        for (int i = 0; i <= n; i++) neighbors.add(new ArrayList<>());
        for (int i = 0; i < n - 1; i++) {                  // edges have no direction
            int u = scan.nextInt();
            int v = scan.nextInt();
            neighbors.get(u).add(v);
            neighbors.get(v).add(u);
        }
        scan.close();

        // Breadth-first from node 1: a parent is always created before its children.
        Tree[] built = new Tree[n + 1];
        int[] depth = new int[n + 1];
        boolean[] seen = new boolean[n + 1];
        ArrayDeque<Integer> queue = new ArrayDeque<>();

        built[1] = new TreeNode(values[1], colors[1], 0);  // the root is never a leaf (n >= 2)
        seen[1] = true;
        queue.add(1);
        while (!queue.isEmpty()) {
            int parent = queue.poll();
            for (int child : neighbors.get(parent)) {
                if (seen[child]) continue;
                seen[child] = true;
                depth[child] = depth[parent] + 1;
                boolean isLeaf = neighbors.get(child).size() == 1;   // only connected to its parent
                built[child] = isLeaf
                        ? new TreeLeaf(values[child], colors[child], depth[child])
                        : new TreeNode(values[child], colors[child], depth[child]);
                ((TreeNode) built[parent]).addChild(built[child]);
                if (!isLeaf) queue.add(child);
            }
        }
        return built[1];
    }
// ---- end of your code ----

    public static void main(String[] args) {
      	Tree root = solve();
		SumInLeavesVisitor vis1 = new SumInLeavesVisitor();
      	ProductOfRedNodesVisitor vis2 = new ProductOfRedNodesVisitor();
      	FancyVisitor vis3 = new FancyVisitor();

      	root.accept(vis1);
      	root.accept(vis2);
      	root.accept(vis3);

      	int res1 = vis1.getResult();
      	int res2 = vis2.getResult();
      	int res3 = vis3.getResult();

      	System.out.println(res1);
     	System.out.println(res2);
    	System.out.println(res3);
	}
}
