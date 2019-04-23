# Quiz 5 - Assessment Questions on 'Practicing Graph Analytics in Neo4j With Cypher'

### 1. What is the number of nodes returned?

- 50,000
- 9656
- 9756
- 8673

### 2. What’s the number of edges?

- 50,000
- 49,834
- 46,621
- None of the above

### 3. The number of loops in the graph is:

- 1035
- 1395
- 1221
- 1243

### 4. The query match (n)-[r]->(m) where m <> n return distinct n, m, count(r) gives us

- the count of all non loop edges between every adjacent node pair.
- the count of all edges between every adjacent node pair.
- the count of all edges.
- None of the above

### 5. The query match (n)-[r]->(m) where m <> n return distinct n, m, count(r) as myCount order by myCount desc limit 1 produces what?

- a random edge
- the node with the maximum number of looping edges
- two neighboring nodes, each with a high outdegree
- the pair of nodes with the maximum number of multi-edges between them

### 6. The query match p=(n {Name:'BRCA1'})-[:AssociationType*..2]->(m) return p produces what?

- The neighbors of the node whose name is ‘BRCA1’
- The 2-neighborhood of the node whose name is ‘BRCA1’
- The neighbors’ neighbors of the node whose name is ‘BRCA1’
- The neighbors whose distance is greater than 1 and less than 2 of the node whose name is ‘BRCA1’

### 7. How many non-directed shortest paths are there between the node named ‘BRCA1’ and the node named ‘NBR1’?

- 8
- 9
- 10
- None of the above

### 8. The top 2 nodes with the highest outdegree are:

- GRB2 and TP53
- EP300 and BRCA1
- MEPCE and EGFR
- SNCA and BRCA1

### 9. Applying the example queries provided to you, create the degree histogram for the network. How many nodes in the graph have a degree of 3?

- 1351
- 821
- 675
- 512