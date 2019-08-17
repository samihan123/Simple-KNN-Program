# Simple-KNN-Program
\nFollowing is simple K - Nearest Neighbors program to classify the cordinates as in to specific class (bad good average)

\nknn.py file consists of program having KNN algorithm which is use for classification and regression predictive problems

\nFollowing is the pseudocode for the Above Program

\n1. According to classes of classifiers , classify the graph . In this program it is been classified into Good, Bad, Average.
\n2. Iterate through dataset and fill the array for the classification
\n3.Take x,y cordinates and K ie distance
\n4.Calculate “d(x, xi)” i =1, 2, ….., n; where d denotes the Euclidean distance between the points.
\n5.Arrange the calculated n Euclidean distances in non-decreasing order.
\n6.Let k be a +ve integer, take the first k distances from this sorted list.
\n.Find those k-points corresponding to these k-distances.
\n8.Display Ans ie Bad, Good, Average which has most number of most nearest class.
