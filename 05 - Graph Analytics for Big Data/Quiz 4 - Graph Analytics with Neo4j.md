# Quiz 4  - Graph Analytics with Neo4j

### 1. Which of the following is a Cypher command used to combine two or more query results?

- union
- combine
- merge
- return

### 2. For a graph network whose nodes are all of type "MyNode", which has both incoming and outgoing edges, and which has both root and leaf nodes, what will the following Cypher code return in a Neo4j report?

```
match (n:MyNode)<-[r]-() return n
```

- All nodes and edges except leaf nodes and their edges.
- The entire network, all nodes and edges
- All nodes except root nodes.
- Edges but no nodes.

### 3. The Cypher query language shares some commands in common with SQL.

- True
- False

### 4. The following query will return a graph containing whatever loops might exist.

```
match (n)-[r]-(n) return n, r
```

- True
- False

### 5. Which Cypher pattern is used to represent a node?

- ()
- []
- {}
- <>

### 6. QNeo4j is a ...

- Graph database
- Relational database
- None of the above

### 7. Which Cypher command launches a Neo4j database search?

- MATCH
- RETURN
- CREATE
- None of the above

### 8.Cypher does not include a specific command to find the shortest path in a graph network.

- False
- True

### 9. Cypher includes a 'diameter' command to find the longest path in a graph network.

- False
- True