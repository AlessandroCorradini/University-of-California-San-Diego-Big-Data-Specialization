# Graphs in Everyday Life - Assignment Part II

Below create a numbered list with the 3 analysis questions you would ask of this graph. For each question, include a 2-5 sentences talking a bit more about the question, how you think you could do the analysis (e.g. find a best path from X to Y where the edges contain Z), and why it is interesting.

I thought a simple Social Network with a basic functionality such as create posts, comments them, ask friendship, chat and likes pages. Below the lists of nodes and edges.

A Social Network like this could provide tons of questions and answers, for example:

- Who are the influencer of the network? Users with lots of friends and Pages with lots of likes are the best candidates to be defined as such. A useful metric is Degree of Centrality.

- What are the trending topic/posts? We can retrieve the trending topic based on the numbers of interactions such comments and likes and compute TF-IDF for each returned comment.

- What are the most active Users? Users (or Pages) with N likes or comments X day (maybe 10?) is very active!

- What are the suggested Users for each User? We should find the closest non-friend neighbors and suggest to each user respectively.

- What are the trending topic/posts?