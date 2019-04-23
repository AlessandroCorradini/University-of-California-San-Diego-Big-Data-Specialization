# Quiz 6 - Using GraphX

### 1. In this code snippet below from the Hands On exercise on importing data, '100L + row...' adds 100 to the value of every country ID. Which of the following statements are true regarding this decision? (Note: you may select more than one)

```
val countries: RDD[(VertexId, PlaceNode)] =
  sc.textFile("./EOADATA/country.csv").
    filter(! _.startsWith("#")).
    map {line =>
      val row = line split ','
      (100L + row(0).toInt, Country(row(1)))
    }
```

- Another option would have been to add 100 to the metropolis keys as they were imported, and leave the country keys as they were originally numbered.
- This step was needed to create unique keys between the country and the metropolis datasets.
- Another option would be to add 500 to the country keys.


### 2. In the metro example, what is an in-degree in relation to a country? Hint: this was covered in the Building a Degree Histogram Hands On exercise.

- A street in a city.
- Another city.
- A continent.
- A metro area or metropolis.

### 3. In the Hands On exercise on network connectedness and clustering, Antarctica was easy to identify. Why?

- It had many edges
- It had a vertex ID of 205.
- It is the green dot that that has no connections, or it is the least connected cluster.

### 4. In the Facebook graph example, the visualization looked like broccoli. Why?

- In a directed graph, the stalks are large.
- Social networks have communities or pockets of people who interact densely.
- The high centrality of some people nodes in facebook gives the graph its broccoli shape.