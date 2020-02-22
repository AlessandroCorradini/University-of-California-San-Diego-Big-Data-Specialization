# Quiz 4  - Hands-On with Splunk

### 1. Which of the queries below will return the average population of the counties in Georgia (be careful not to include the population of the state of Georgia itself)?

- None of the above
- source="census.csv" CTYNAME != "Georgia" STNAME="Georgia" | stats sum(CENSUS2010POP)
- **source="census.csv" CTYNAME != "Georgia" STNAME="Georgia" | stats mean(CENSUS2010POP)**
- source="census.csv" STNAME="Georgia" | stats mean(CENSUS2010POP)

### 2. What is the average population of the counties in the state of Georgia (be careful not to include the population of the state of Georgia itself)?

- 394383.53786
- 45373.454788
- 243767.4564
- **60928.635220**

### 3. Of the options below, which query allows you to find the state with the most counties?

- source="census.csv" | stats count by CENSUS2010POP | sort count
- stats count by STNAME | sort -count
- source="census.csv" | stats count by CTYNAME | sort num(count)
- **source="census.csv" | stats count by STNAME | sort count desc**

### 4. What state contains the most counties?

- **Texas**
- California
- Georgia
- Alaska

### 5. Of the options below, which query allows you to find the most populated counties in the state of Texas?

- STNAME="Texas" CENSUS2010POP > 100000 | sort -CENSUS2010POP | table CENSUS2010POP,CTYNAME
- STNAME="Texas" CENSUS2010POP > 100000 | sort CENSUS2010POP desc | table CENSUS2010POP,CTYNAME
- **Both**
- Neither

### 6. What is the most populated county in the state of Texas?

- **Harris**
- Dallas
- Travis
- Bexar