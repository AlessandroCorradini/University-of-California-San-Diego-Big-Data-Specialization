MapReduce is the core programming model for the Hadoop Ecosystem. We’ve found it’s really helpful to walk through the steps of MapReduce for yourself in order to internalize how it really works. In video lecture, we walked through the steps of MapReduce to count words -- our keys were words. In this exercise, we’ll have you count shapes -- the keys will be shapes.

Note: This assignment can be done in PPT and printed to PDF or on paper and submitted as a picture. Template in PPT, template in JPG.

[Slide1.jpg](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/_68e7a7ac4eb311090cdfe58fce4322d2_Slide1.jpg?expiry=1555545600000&hmac=6UhOGcoJY6mXGt6h_AUSPc8Ojkar8QZYHjHozms1dtk)

[PeerReviewforUpload.pptx](https://d3c33hcgiwev3.cloudfront.net/_86c448dfa47cdab170075f16cd25c650_PeerReviewforUpload.pptx?Expires=1555545600&Signature=Pn5EzRJA1QXj5EDF0JdgKA3hXE5RF90M42clLzxlxRzDo9mQpaOli8EPF9pLQe96t41tiBt-Uh9s2iOHxHWPRihEigD9OhLKxsNnhW7gMuDalgDSbw9GwVxz8L6fkxe~eeZYsiFPdG9wtPRK3cQ0W7BST6gkZAcPragfmIJSc3o_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/n2lTP9LIEeWJYg65RLEZEQ_7d239771665703de4da6c46403bab1db_Slide1.jpg?expiry=1555545600000&hmac=_n8rX14qCZhLWpf_urXCOivMvdEAJNWt7f5Wq4TDp8I)

Your job is to perform the steps of MapReduce to calculate a count of the number of squares, stars, circles, hearts and triangles in the dataset shown in the picture above. You should follow the steps of MapReduce as they were explained in [this video](https://www.coursera.org/learn/big-data-introduction/lecture/pL4NH/mapreduce-simple-programming-for-big-results).

**Step 0:** Store the dataset across 4 partitions in HDFS. **Note: we have already done one partition for you. Hint: Balance the load, but there is more than on possible “correct” partitioning.**

**Step 1:** Map the data. **Hint: Mapping involves clustering like keys together. Show this in the visual placement of keys within a partition.**

**Step 2:** Sort and Shuffle. **Note: as mentioned in lecture, you don’t have to use the same number of nodes in this step as you did before. Let’s use three instead. Hint: Balance the load.**

**Step 3:** Reduce to calculate the final counts. **Hint: Fill in the blank lines to finalize the key-value pairs**

**Modification: Simplify drawing the key-value pair**

The “Map” stage of MapReduce generates key-value pairs. For example, in the video we saw:

```
my, my \->  (my, 1), (my,1)
```

Showing that two instances of the word “my” would get mapped to two key-value pairs. You might have noticed that until the Reduce step, the value in all key-value pairs is 1. To make this activity less cluttered visually, we will have you leave out the “,1” part of each key-value pair, and just represent a key-value pair with the appropriate image.

**Review criteria**

You will be reviewed based on:

*   Whether your steps appropriately document data movement or analysis in Steps 0-2 (see hints in Step descriptions above).
*   You get correct final counts in Step 3. (Yes, we know you can count – but it’s the process!)

Note: More than one single "correct" answer exists for this assignment.