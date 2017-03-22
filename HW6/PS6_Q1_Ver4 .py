#!/usr/bin/python
#Zhaozhong Peng , Sibo Song, Yongbo Shu
#2017/3/15 (Version 1)
#2017/3/17 (Version 2)
#2017/3/21 (Version 3) change whole function to random selet path
#2017/3/22 (Version 4) Fix bug
## Function TreeSearchingRouts still need testing(running time is toooooooo long, but works on x='polynomial' y='exponential'
## Also currently if L=10, function infinityMonkey will only return monkeys failed, according to infinity monkey theroy, the
## probility that monkeys success is too small at about (1/26)^10 for each time (consider the frequency is equal for all alphabet). 
## But if I change the L to 5 then will get a success signal. XD
import numpy
import random
import sys   
sys.setrecursionlimit(1000000000)	

def cost(A,x,y) :   #calculate the cost
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
	
def alignStrings(x,y) :  #creat a table with strings and cost
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
	
	
def determineOptimalOp(A,x,y): #determin the next step
        options=[]
        indel=1
        swap=10
        sub=10
        no_op=0
        if(x==1 and y==1):
            options.append([0,0,'start'])
            return options
        if(x==1):
            options.append([x,y-1,'Delete a string in x'])
            return options
        if(y==1):
            options.append( [x-1,y,'Delete a string in y'])
            return options
        if(A[0][y]==A[x][0]):
            options.append([x-1,y-1,'Not doing anything in this position'])
            return options
        if(x-2>=1 and y-2>=1):
            minValue=min(A[x-1][y],A[x][y-1],A[x-2][y-2],A[x-1][y-1])
            if (minValue==A[x-2][y-2] and minValue+swap==A[x][y]):
                options.append([x-2,y-2,'Swap the elements between this position and last position in x,y'])
                if(minValue==A[x-1][y-1] and minValue+sub==A[x][y]):
                    options.append([x-1,y-1,'Delete both element in this position in x,y'])
                    if(minValue==A[x-1][y] and minValue+indel==A[x][y]):
                        options.append([x-1,y,'Insert a gap in to string x'])
                    if(minValue==A[x][y-1] and minValue+indel==A[x][y]):
                        options.append([x,y-1,'Insert a gap in to string y'])
                    return options
                minValue==min(A[x-1][y],A[x][y-1])
                if(minValue==A[x-1][y] and minValue+indel==A[x][y]):
                    options.append([x-1,y,'Insert a gap in to string x'])
                if(minValue==A[x][y-1] and minValue+indel==A[x][y]):
                    options.append([x,y-1,'Insert a gap in to string y'])
                return options
            minValue=min(A[x-1][y],A[x][y-1],A[x-1][y-1])
            if (minValue==A[x-1][y-1] and minValue+sub==A[x][y]):
                options.append([x-1,y-1,'Delete both element in this position in x,y'])
                if (minValue==A[x][y-1] and minValue+indel==A[x][y]):
                    options.append([x,y-1,'Insert a gap in to string y'])
                if (minValue==A[x-1][y] and minValue+indel==A[x][y]):
                    options.append([x-1,y,'Insert a gap in to string x'])
                return options
            minValue=min(A[x-1][y],A[x][y-1])
            if(minValue==A[x-1][y] and minValue+indel==A[x][y]):
                options.append([x-1,y,'Insert a gap in to string x'])
            if(minValue==A[x][y-1] and minValue+indel==A[x][y]):
                options.append([x,y-1,'Insert a gap in to string y'])
            return options
    minValue=min(A[x-1][y],A[x][y-1],A[x-1][y-1])
    if (minValue==A[x-1][y-1] and minValue+sub==A[x][y]):
        options.append([x-1,y-1,'Delete both element in this position in x,y'])
        if (minValue==A[x][y-1] and minValue+indel==A[x][y]):
            options.append([x,y-1,'Insert a gap in to string y'])
        if(minValue==A[x-1][y] and minValue+indel==A[x][y]):
            options.append([x-1,y,'Insert a gap in to string x'])
        return options
    minValue=min(A[x-1][y],A[x][y-1])
    if(minValue==A[x-1][y] and minValue+indel==A[x][y]):
        options.append([x-1,y,'Insert a gap in to string x'])
    if(minValue==A[x][y-1] and minValue+indel==A[x][y]):
        options.append([x,y-1,'Insert a gap in to string y' ])
    return options
		
def extractAlignment(S) : #return how to change the x
	inverseRoute=[]
	route=[]
	inverseOperations=[]
	operations=[]
	x=len(S)-1
	y=len(S[0])-1
	inverseRoute.append([x,y])
	while (x>=1 or y>=1):
		targets=determineOptimalOp(S,x,y)
		updateIndices=random.randint(0,len(targets)-1)
		choice=targets[updateIndices]
		inverseOperations.append(choice[2])
		x=choice[0]
		y=choice[1]	
	for i in range (0,len(inverseOperations)):
		operations.append(inverseOperations[len(inverseOperations)-1-i])
	return operations


def commonSubstrings(x,L,a):
        substring=[]
        x=list(x)
        string=''
        indexOfx=0
        swaped=False
        for i in range (1,len(a)):
            if(a[i]=='Swap the elements between this position and next position in x'):
                tmp=x[indexOfx+1]
                x[indexOfx+1]=x[indexOfx]
                x[indexOfx]=tmp
                string=''
                swaped=True	
                indexOfx=indexOfx+1
            if(a[i]=='Delete a string in x'):
                del x[indexOfx]
                x.insert(indexOfx,'-')
                if(len(string)>=L):
                    substring.append(string)
                string=''
                swaped=False
                indexOfx=indexOfx+1
            if(a[i]=='Insert a gap in to string x'):  
                x.insert(indexOfx,'-')
                if(len(string)>=L):
                    substring.append(string)
                string=''
                swaped=False
                indexOfx=indexOfx+1
            if(a[i]=='Insert a gap in to string y'):
                del x[indexOfx]
                if(len(string)>=L):
                    substring.append(string)
                swaped=False
                string=''
            if(a[i]=='Not doing anything in this position'):
                if(swaped==False):
                    string=string+x[indexOfx]		
                indexOfx=indexOfx+1
            if(a[i]=='Delete both element in this position in x,y'):
                del x[indexOfx]
                x.insert(indexOfx,'-')
                if(len(string)>=L):
                    substring.append(string)
                swaped=False
                string=''
                indexOfx=indexOfx+1
        if(len(string)>=L):
            substring.append(string)
        x=''.join(x)
        return substring,x  ###important, don't print the list directly, use for loop to print each element
#####################QUESTION(C)#############################
def TreeSearchingRouts(A,x,y,routeCount):
	count=routeCount
	leftBranch=0
	rightBranch=0
	subBranch=0
	swapBranch=0
	indel=1
	swap=10
	sub=1
	judge=0
	if(x==1 or y==1):
		return count+1
	if(A[0][y]==A[x][0]):
		no_op=TreeSearchingRouts(A,x-1,y-1,count)
		return no_op
	if(x-2>=1 and y-2>=1):
		minValue=min(A[x-1][y],A[x][y-1],A[x-2][y-2],A[x-1][y-1])
		if (minValue==A[x-2][y-2] and minValue+swap==A[x][y]):
			judge=1
			swapBranch=TreeSearchingRouts(A,x-2,y-2,count)
		if (judge==0):
			minValue=min(A[x-1][y],A[x][y-1],A[x-1][y-1])
		if (minValue==A[x-1][y-1] and minValue+sub==A[x][y]):
			judge=1
			subBranch=TreeSearchingRouts(A,x-1,y-1,count)
		if (minValue==A[x][y-1] and minValue+indel==A[x][y]):
			leftBranch=TreeSearchingRouts(A,x,y-1,count)
		if (minValue==A[x-1][y] and minValue+indel==A[x][y]):
			rightBranch=TreeSearchingRouts(A,x-1,y,count)
		return leftBranch+rightBranch+subBranch+swapBranch
	minValue=min(A[x-1][y],A[x][y-1],A[x-1][y-1])
	if (minValue==A[x-1][y-1] and minValue+sub==A[x][y]):
		subBranch=TreeSearchingRouts(A,x-1,y-1,count)
	if (minValue==A[x][y-1] and minValue+indel==A[x][y]):
		leftBranch=TreeSearchingRouts(A,x,y-1,count)
	if (minValue==A[x-1][y] and minValue+indel==A[x][y]):
		rightBranch=TreeSearchingRouts(A,x-1,y,count)
	return leftBranch+rightBranch+subBranch

########################QUESTION(f)#############################

def freqTXTexchanger():
	freqList=[]
	thefile=open("x1.txt")
	line=thefile.readline()
	if(len(line.split())==3):
		word=" "
		freq=int(line.split()[2])
	else:
		word=line.split()[0]
		freq=int(line.split()[1])
		word=list(word)
		word=word[1]
	freqList.append([word,freq])
	while line :
		line=thefile.readline()
		if(len(line.split())==3):
			word=" "
			freq=int(line.split()[2])
		if(len(line.split())==2):
			word=line.split()[0]
			freq=int(line.split()[1])
			word=list(word)
			word=word[1]
		freqList.append([word,freq])		
	return freqList

def randomInputByMonkey(freqList,n):
	monkeyTXT=""
	for i in range (0,len(freqList)):
		for j in range (0, freqList[i][1]):
			monkeyTXT=monkeyTXT+freqList[i][0]
	monkeyTXT=list(monkeyTXT)
	random.shuffle(monkeyTXT)
	monkeyTXT=''.join(monkeyTXT)
	Highest_n=len(monkeyTXT)
	firstNthMonkeyTXT=""
	for i in range (0,n):
		firstNthMonkeyTXT=firstNthMonkeyTXT+monkeyTXT[i]		
	return firstNthMonkeyTXT,Highest_n

def infinityMonkey(compairTXT,L):
	freqList=freqTXTexchanger()
	for i in range (0,randomInputByMonkey(freqList,0)[1]):
		realOutput=randomInputByMonkey(freqList,i)[0]
		align=alignStrings(realOutput,compairTXT)
		operations=extractAlignment(align)
		answer=commonSubstrings(realOutput,L,operations)
		if(len(answer[0])!=0):
			print "Monkeys did it! they input a correct string with lenth ",L," and the needed n is ",i
			return
	print "Monkeys didn't make it."
	return  


####################TEST AREA########################
#thefile=open("x.txt")
#thefile1=open("y.txt")
#x=thefile.readline()
#y=thefile1.readline()
#x='polynomial'
#y='exponential'
#S=alignStrings(x,y)
#print "input: x=",x," y=",y
#print "cost map:"
#print numpy.array(S)
#print "lowest cost:"
#print S[len(S)-1][len(S[0])-1]
#print "the operations:"
#operations=extractAlignment(S)
#for i in range(0,len(operations)):
#	print operations[i]
#print "Local Alignment:"
#answer=commonSubstrings(x,10,operations)
#print answer[1]
#print "Let L=10"
#print answer[0]
########################QUESTIONc###################
#print "Number of best way to change:"
#print TreeSearchingRouts(S,len(S)-1,len(S[0])-1,0)
########################QUESTIONf####################
#thefile=open("y1.txt")
#y=thefile.readline()
#infinityMonkey(y)
