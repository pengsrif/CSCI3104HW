#!/usr/bin/python
#Zhaozhong Peng
#2017/3/15
#reminder: the time complexity should be n^4, so this might not be the best choice

import numpy

def currentMaxPoint(A,x,y):                                             #x is row y is colum
	if (x!=len(A)-1 and y!=len(A)-1 and x!=0 and y!=0 ):                    #when start point is not on border
		pointMap=[]                                                     #creat a new matrix start with index x,y store the highest point can get
		rows=len(A)-x
		colums=len(A)-y
		for i in range (0,rows):                                        #creat a 2D array with all 0
			row=[]
			for j in range (0,colums):	
				row.append(0)
			pointMap.append(row)
		pointMap[0][0]=A[x][y]                                          #store the first element
		for i in range (0,rows):                                        # calculate the point can get when reach the border, in this position, ignore A[len(x)-1][len(A)-1] because you cannot get to that point if is not the starting point
			if(i!=rows-1):                                              #store the values exclude the last row
				for j in range (0, colums):
					if (i==0):                                          #store the first row
						if (j!=0):                                      #first element already exist so skip it 
							pointMap[i][j]=pointMap[i][j-1]+A[x+i][y+j]	
					if (i!=0):
						if (j==0 and colums!=1):                        #store first colum
							pointMap[i][j]=pointMap[i-1][j]+A[x+i][y+j]	
						if (j!=0 and j!= colums-1):                     #store the values between first and last colum
							pointMap[i][j]=max(pointMap[i-1][j]+A[x+i][y+j],pointMap[i][j-1]+A[x+i][y+j])
						if (j==colums-1):                               #store the last colum
							pointMap[i][j]=pointMap[i][j-1]+A[x+i][y+j]
						#print numpy.array(pointMap)	
			else:
				for j in range (0,colums):                              #store the last row
					if(j!=colums-1):                                    #do except the last colum
						pointMap[i][j]=pointMap[i-1][j]+A[x+i][y+j]
			pointMap[rows-1][colums-1]=A[len(A)-1][len(A)-1]	
		maxPoint=A[len(A)-1][len(A)-1]
		for i in range (0,rows-1):
			maxPoint=max(pointMap[i][colums-1],maxPoint)
		for j in range (0,colums-1):
			maxPoint=max(pointMap[rows-1][j],maxPoint)
		#print maxPoint
		#return pointMap
		print numpy.array(pointMap)
		return maxPoint
	else:                                                               # if the start point is on border, game stop return current value
		print "at edge"
		#print A[x][y]
		return A[x][y]
				
	


def findHighestPoint(A):
	HighestPoint=A[len(A)-1][len(A)-1]
	for i in range (0,len(A)): #do the currentMaxPoint function at every point to find the max value can get in the game
		for j in range (0, len(A)):
			HighestPoint=max(HighestPoint,currentMaxPoint(A,i,j))
	print HighestPoint

########################### TEST AREA #########################################
A=[[-1,7,-8,10,-5],[-4,-9,8,-6,0],[5,-2,-6,-6,7],[-7,4,7,-3,-3],[7,1,-6,4,-9]]
findHighestPoint(A)
#currentMaxPoint(A,1,2)
