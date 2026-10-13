# HackerRank: BFS: Shortest Reach in a Graph

**Type:** HackerRank graph challenge
**Source:** [BFS: Shortest Reach in a Graph](https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem)
**Focus:** adjacency lists, breadth-first search, disconnected nodes, complexity

## Exercise

For each undirected, unweighted graph, return the shortest distance from a start node to every other node in ascending node order. Each edge contributes distance `6`; unreachable nodes use `-1`.

Example input contains one query:

```text
1
5 3
1 2
1 3
3 4
1
```

Starting at node 1, nodes 2 and 3 are one edge away, node 4 is two edges away, and node 5 is disconnected. Expected output:

```text
6 6 12 -1
```

## Solution

The function below is the core implementation; adapt its signature to the HackerRank language stub.

```java
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

static List<Integer> bfs(int nodeCount, List<List<Integer>> edges, int start) {
    List<List<Integer>> adjacency = new ArrayList<>(nodeCount + 1);
    for (int node = 0; node <= nodeCount; node++) {
        adjacency.add(new ArrayList<>());
    }

    for (List<Integer> edge : edges) {
        int left = edge.get(0);
        int right = edge.get(1);
        adjacency.get(left).add(right);
        adjacency.get(right).add(left);
    }

    int[] distance = new int[nodeCount + 1];
    Arrays.fill(distance, -1);
    distance[start] = 0;

    Queue<Integer> queue = new ArrayDeque<>();
    queue.offer(start);
    while (!queue.isEmpty()) {
        int current = queue.poll();
        for (int neighbor : adjacency.get(current)) {
            if (distance[neighbor] == -1) {
                distance[neighbor] = distance[current] + 6;
                queue.offer(neighbor);
            }
        }
    }

    List<Integer> result = new ArrayList<>(nodeCount - 1);
    for (int node = 1; node <= nodeCount; node++) {
        if (node != start) {
            result.add(distance[node]);
        }
    }
    return result;
}
```

Marking a node when it is enqueued ensures each node enters the queue once. The graph is undirected, so add both adjacency directions.

**Complexity:** $O(V + E)$ time and space.
