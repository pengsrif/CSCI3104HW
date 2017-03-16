#!/usr/bin/python
#Zhaozhong Peng
#2017/3/15
#currently is test version so there is no commit

import numpy
	
def cost(A,x,y) :  ## x is row y is colum
	indel=1
	swap=10
	sub=1
	no_op=0
	if(x==1 and y==1):
		return 0
	if(x==2 and y==2):
		return min(int(A[1][2])+indel,int(A[2][1])+indel,int(A[1][1])+sub)
	if(x==1 and y!=1):
		return A[x][y-1]+1
	if(y==1 and x!=1):
		return A[x-1][y]+1
	if(A[0][y]==A[x][0]):
		if(y-2>=1 and x-2>=1):
			return min(int(A[x-2][y-2])+swap,int(A[x-1][y-1])+no_op,int(A[x-1][y])+indel,int(A[x][y-1])+indel)
		return min(int(A[x-1][y-1])+no_op,int(A[x-1][y])+indel,int(A[x][y-1])+indel)
	else:
		if(y-2>=1 and x-2>=1):
			return min(int(A[x-2][y-2])+swap,int(A[x-1][y-1])+sub,int(A[x-1][y])+indel,int(A[x][y-1])+indel)
		return min(int(A[x-1][y-1])+sub,int(A[x-1][y])+indel,int(A[x][y-1])+indel)
	
def alignStrings(x,y) : 
	x=" "+x
	y=" "+y
	S=[]
	S.append(['/'])
	for i in range (0,len(x)):
		S[0].append(x[i])
	for i in range (1,len(y)+1):
		S.append([y[i-1]])
		for j in range (0,len(x)):
			S[i].append(0)
	for i in range (1,len(y)+1):
		for j in range (1,len(x)+1):
			S[i][j]=cost(S,i,j)
	return S 		
	
	
def determineOptimalOp(A,x,y): 
	indel=1
	swap=10
	sub=1
	no_op=0
	if(x==1 and y==1):
		return [0,0,'start']
	if(x==1):
		return [x,y-1,'Delete a string in x']
	if(y==1):
		return [x-1,y,'Delete a string in y']
	if(A[0][y]==A[x][0]):
		return [x-1,y-1,'Not doing anything in this position']
	if(x-2>=1 and y-2>=1):
		minValue=min(A[x-1][y],A[x][y-1],A[x-2][y-2],A[x-1][y-1])
		if (minValue==A[x-2][y-2] and minValue+swap==A[x][y]):
			return [x-2,y-2,'Swap the elements between this position and last position in x,y']
		minValue=min(A[x-1][y],A[x][y-1],A[x-1][y-1])
		if (minValue==A[x-1][y-1] and minValue+sub==A[x][y]):
			return [x-1,y-1,'Delete both element in this position in x,y']
		if (minValue==A[x][y-1] and minValue+indel==A[x][y]):
			return [x,y-1,'Insert a gap in to string y' ]
		return [x-1,y,'Insert a gap in to string x']
	minValue=min(A[x-1][y],A[x][y-1],A[x-1][y-1])
	print str(A[x][y])+' to '+str(minValue)
	if (minValue==A[x-1][y-1] and minValue+sub==A[x][y]):
		return [x-1,y-1,'Delete both element in this position in x,y']
	if (minValue==A[x][y-1] and minValue+indel==A[x][y-1]):
		return [x,y-1,'Insert a gap in to string y']
	return [x-1,y,'Insert a gap in to string x']
		
def extractAlignment(S) :
	#print numpy.array(S)
	inverseRoute=[]
	route=[]
	inverseOperations=[]
	operations=[]
	x=len(S)-1
	y=len(S[0])-1
	inverseRoute.append([x,y])
	while (x>=1 or y>=1):
		target=determineOptimalOp(S,x,y)
		#direction=[]
		#direction.append(target[0])
		#direction.append(target[1])
		inverseOperations.append(target[2])
		#S[x][y]=-1
		x=target[0]
		y=target[1]
		#if(target!=[0,0,'start']):
		#	inverseRoute.append(target)
	#print numpy.array(S)
	for i in range (0,len(inverseOperations)):
		#route.append(inverseRoute[len(inverseRoute)-1-i])
		operations.append(inverseOperations[len(inverseOperations)-1-i])
	#return route,operations
	return operations

def commonSubstrings(x,L,a):
	substring=[]
	x=list(x)
	counter=0
	string=''
	for i in range (0,len(a)):
		if(a[i]=='Delete a string in x' or a[i]=='Insert a gap in to string y' ):
			del x[i-1]
			x.insert(i-1,'-')
			if(counter>=L):
				substring.append(string)
			counter=0
			string=''
			#print x,i
		if(a[i]=='Delete a string in y' or a[i]=='Insert a gap in to string x'):
			x.insert(i-1,'-')
			if(counter>=L):
				substring.append(string)
			counter=0
			string=''
			#print x,i
		if(a[i]=='Not doing anything in this position'):
			counter=counter+1
			string=string+x[i-1]
			if(i==len(a)-1 and counter>=L):
				substring.append(string)
			#print x	,i				
		if(a[i]=='Delete both element in this position in x,y'):
			del x[i-1]
			x.insert(i-1,'-')
			if(counter>=L):
				substring.append(string)
			counter=0
			string=''
			#print x,i
	x=''.join(x) 
	return substring,x 

x='polynomial'
y='exponential'
#S=alignStrings(x,y)
#print (S[len(y)][len(x)])
operations=extractAlignment(alignStrings(x,y))

print "input: x=",x," y=",y
print "the operations:"
for i in range(0,len(operations)):
	print operations[i]
print "Local Alignment:"
answer=commonSubstrings(x,2,operations)
print answer[1]
print "Let L=2"
print answer[0]
