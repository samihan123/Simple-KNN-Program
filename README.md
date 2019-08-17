# Simple-KNN-Program
Following is simple K - Nearest Neighbors program to classify the cordinates as in to specific class (bad good average)

knn.py file consists of program having KNN algorithm which is use for classification and regression predictive problems

Following is the pseudocode for the Above Program

1. According to classes of classifiers , classify the graph . In this program it is been classified into Good, Bad, Average.
2. Iterate through dataset and fill the array for the classification
3.Take x,y cordinates and K ie distance
4.Calculate “d(x, xi)” i =1, 2, ….., n; where d denotes the Euclidean distance between the points.
5.Arrange the calculated n Euclidean distances in non-decreasing order.
6.Let k be a +ve integer, take the first k distances from this sorted list.
7.Find those k-points corresponding to these k-distances.
8.Display Ans ie Bad, Good, Average which has most number of most nearest class.
