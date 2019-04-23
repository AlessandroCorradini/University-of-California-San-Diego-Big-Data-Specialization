# Classifying in KNIME to identify big spenders in Catch the Pink Flamingo

 Predicting which user is likely to purchase big-ticket items while playing Catch the Pink Flamingo is valuable knowledge to have for Eglence since in-app purchases are a major source of revenue. In this assignment, you will analyze available data to classify users as buyers of big-ticket items (“HighRollers”) vs. buyers of inexpensive items (“PennyPinchers”). Big-ticket items are those with a price of more than $5.00, and inexpensive items are those that cost $5.00 or less.

A data file named “combined\_data.csv” has been created for this assignment. This file has some data derived from the log files. The contents of this file are described in [this reading](https://www.coursera.org/learn/big-data-project/supplement/5iPBb/description-of-combined-data-csv-file).

You will build a KNIME workflow to perform analysis for this classification problem. Note: As you go along, be sure to update node names (.e.g text below nodes) and workflow annotation.

Along the way you will be creating parts of your appendix for the final project which outlines your findings explains how you perform this classification problem.

**Setup**

Be sure to read [“Workflow Overview: Building a Decision Tree in KNIME”](https://www.coursera.org/learn/big-data-project/supplement/5IEPD/workflow-overview-for-building-a-decision-tree-in-knime) before beginning this assignment. Start with the sample decision tree workflow referred to in that reading. You will modify this workflow as you perform the tasks for this assignment. **NOTE:** All the nodes you need for the workflow to complete this assignment is described in that reading.

**Step 1: Data Preparation**

The first step is to read in the data and prepare it for modeling in KNIME. Below is an overview of the steps you will need to take. Download and fill in this template ([word](https://drive.google.com/file/d/0B16gFG_FlhmqOHV2aUJ6dU81Rnc/view?usp=sharing)) as you complete these steps (the completed template will be used as a part of your technical appendix for your final project):

1.  Read in the data from the file combined\_data.csv. Identify the number of samples.
2.  Filter samples (i.e., rows) to only contain those with purchases and identify that number. NOTE: You will need to add a new node to your KNIME workflow for this. The new node should be placed between the File Reader and Color Manager nodes.
3.  Create a new categorical attribute for the target. This new categorical attribute will be derived by binning an existing numeric attribute. Remember that for this project, we want to define two categories for price which we will use to distinguish between HighRollers (buyers of items that cost more than $5.00) and PennyPinchers (buyers of items that cost $5.00 or less). NOTE: You will need to add a new node to your KNIME workflow for this. This new node should be placed between the node that was added in #2 above and Color Manager. HINT: The type of node you need to add is one of the Data Preparation nodes described in the Workflow Overview for Building a Decision Tree in KNIME reading. Pay close attention to the definitions of HighRollers and PennyPinchers.
4.  Filter the data to only contain the attributes (i.e., columns) that you want to use for your analysis. Hint: There are attributes that can be immediately identified as being inappropriate for this classification task without any analysis; those attributes should be filtered out. NOTE: You will need to add a new node to your KNIME workflow for this. This new node should be placed between the node that was added in #3 above and Color Manager.
5.  Remove nodes Scatter Plot and Interactive Table from the workflow. You will not need those nodes for this assignment.

**Step 2: Data Partitioning and Modeling**

With the prepared data, you are now ready to create your model to predict whether a user is HighRoller or PennyPincher Next you will be building a decision tree. Download and fill in this template ([word](https://drive.google.com/file/d/0B16gFG_FlhmqWkh4LUR0V1A5R2s/view?usp=sharing)) as you complete these steps

1.  Partition the data set into train and test data sets (60% train and 40% test). When doing so, be sure to select "Stratified sampling". Also select "Use random seed", and copy and paste this number for the random seed value: 1466016757670. You can check [this reading](https://www.coursera.org/learn/big-data-project/supplement/5IEPD/workflow-overview-for-building-a-decision-tree-in-knime) for an explanation of Stratified sampling.
2.  Create a decision tree. Be sure to set the decision tree learner node to use pruning for induction (Use MDL for pruning).
3.  Take a screenshot of your resulting decision tree.

**Step 3: Evaluation**

Now that you have your model built and some results, you can assess your model’s performance. Download and fill in this template ([word](https://drive.google.com/file/d/0B16gFG_FlhmqXzItRUM1N1FQUmM/view?usp=sharing)) as you complete these steps

1.  Open the appropriate node to view the confusion matrix and accuracy. Take a screenshot.
2.  Identify the overall accuracy of the model.
3.  Describe what the values in the confusion matrix mean. Be sure to indicate which things are correctly or incorrectly predicted.

**Step 4: Analysis Conclusions**

Create a screenshot of your final KNIME workflow and draw some conclusions and make some recommendations. Download and fill in this template ([word](https://drive.google.com/file/d/0B16gFG_FlhmqZGJxXzMxM0NYTlE/view?usp=sharing)) to guide you.

1.  What makes a user a HighRoller? Draw some insights from your analysis. Hint: Look at the resulting decision tree.
2.  Give 2 recommendations to increase revenue you would propose based on these insights.

A compiled template file with all the template steps can be found here ([word](https://drive.google.com/file/d/0B16gFG_Flhmqc1Z6T3RlQmg1TEE/view?usp=sharing), [PDF](https://drive.google.com/file/d/0B16gFG_FlhmqQ2dkU21wNmRfTms/view?usp=sharing)).
