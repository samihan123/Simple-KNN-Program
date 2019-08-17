import csv
import math

def classifyPoint(points, p, k):
    distance = []
    for groups in points:
        euclidean_distance = math.sqrt((int(groups[0]) - p[0])**2 + (int(groups[1]) - p[1])**2)
        distance.append((euclidean_distance, groups[2]))
    print 'Distance of ' +str(k)+ ' nearest neighbours =>\n'
    distance = sorted(distance)[:k]
    f1 = 0
    f2 = 0
    f3=     0
    for d in distance:
    	if (d[1] == 0):
        	print 'Bad '+str(d[0])
        	f1 = f1 + 1
        elif (d[1] == 1):
        	print 'Good '+str(d[0])
        	f2 = f2 + 1
        elif(d[1]==2):
            print 'Average '+str(d[0])
            f3=f3+1 
    print ' '
    if((f1>f2) & (f1>f3)):
	return "Bad" 
    elif ((f2>f3) & (f2>f1)):
	return "Good" 
    elif((f3>f1) & (f3>f2)):
	return "Average"

#def main():
lines = csv.reader(open("data.csv", "rb"))
input = list(lines)
n = len(input) - 1
for i in input:
	print i
x = int(raw_input("Enter the x of test point: "))
y = int(raw_input("Enter the y of test point: "))
p = (x, y)
k = int(raw_input('Enter the number of neighbours: '))

print ' '
for i in range (1, n+1):
	if(input[i][2] == 'Bad'):
		input[i][2] = 0
        elif(input[i][2]=='Good'):
		input[i][2] = 1
	elif(input[i][2]=='Average'):
		input[i][2]= 2
print ("The value classified to test point is: {}".\
format(classifyPoint(input[1:], p, k)))  #1 to all

#if __name__ == '__main__':
#    main() s
