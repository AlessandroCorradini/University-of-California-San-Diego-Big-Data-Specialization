# Quiz 2 - Postgres, MongoDB and Pandas

### 1. What is the highest level that the team has reached in gameclicks? (Hint: use the MAX operation in postgres).

- 6
- **8**
- 9
- 10
- 7

### 2. How many user id's (repeats allowed) have reached the highest level as found in the previous question? (Hint: For postgres: you may either use two queries or use a sub-query).

- 106436
- 67271
- 122757
- **51294**
- 98823

### 3. How many user id’s (repeats allowed) reached the highest level in game-clicks and also clicked the highest costing price in buy-clicks? Hint: Refer to question 4 for ideas.

- 66887
- **32747**
- 23301
- 73226

### 4. What does the following line of code do in postgres?

SELECT count(userid) FROM (SELECT buyclicks.userId, teamLevel, price FROM buyclicks JOIN gameclicks on buyclicks.userId = gameclicks.userId) temp WHERE price=3 and teamLevel=5;

- Displays the users who have bought items worth $3 and have had a team with level 5.
- This is an invalid line of code, the subquery is not formatted properly.
- Counts the users who exists between both gameclicks and buyclicks files.
- **Finds the total number of user ids (repeats allowed) in buy-clicks that have bought items with prices worth $3 and was in a team with level 5 at some point in time.**

### 5. In the MongoDB data set, what is the username of the twitter account who has a tweet_followers_count of exactly 8973882?

- CreateImga
- Autocenterit
- **FIFAcom**
- SasSpear