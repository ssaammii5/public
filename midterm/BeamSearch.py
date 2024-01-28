import random
Node=[['A',2],['B',1],['C',2],['D',3],['E',3],['F',1],['G',0]]

SuccList ={ 
	'A':[['B',2,1], ['C',1,2], ['D',2,3]],
	'B':[['A',2,2], ['E',3,3]],
	'C':[['A',1,2], ['F',2,1]],
	'D':[['A',2,2], ['G',3,0]],
	'E':[['B',3,1], ['G',4,0]],
	'F':[['C',2,2], ['G',3,0]],
	'G':[['E',4,3], ['F',3,1], ['D',3,3]]
}

Start='A'
Goal='G'
Closed = list()
SUCCESS=True
FAILURE=False
State=FAILURE

def GOALTEST(N):
	if N == Goal:
		return True
	else:
		return False

def MOVEGEN(N):
	New_list=list()
	if N in SuccList.keys():
		New_list=SuccList[N]
	print("New_list=",New_list)
	return New_list
	
def APPEND(L1,L2):
	New_list=L1+L2
	return New_list

def EVAL_SORT(L): #L=[['B',2,1], ['C',1,2], ['D',2,3]]
	L.sort(key = lambda x: x[1]+x[2]) #x=['B',2,1]--> x[1]=2, x[2]=1
	return L

def Bean_Search(Start,beta):
	OPEN=[[Start,2,0]]
	CLOSED=list()
	global State
	global Closed
	i=0
	while (len(OPEN) != 0) and (State != SUCCESS):
		print("------------")
		N= OPEN[0]
		print("N=",N)
		del OPEN[0] #delete the node we picked
		
		if GOALTEST(N[0])==True:
			State = SUCCESS
			CLOSED = APPEND(CLOSED,[list(N)])
			print("CLOSED=",CLOSED)
		else:
			L=[val[0] for val in CLOSED]
			if N[0] not in L:
				CLOSED = APPEND(CLOSED,[list(N)])
				print("CLOSED=",CLOSED)
			CHILD = MOVEGEN(N[0])
			print("CHILD=",CHILD)
			for val in CLOSED:
				if val in CHILD:
					CHILD.remove(val)
			
			#Evaluate each node heurestics
			OPEN = APPEND(CHILD,OPEN) #append movegen elements to OPEN
			EVAL_SORT(OPEN)
			print("OPEN=",OPEN)
			#Take the best ß nodes from Open discarding others
			if (len(OPEN) > beta):
				open=list()
				for i in range(beta):
					open.append(OPEN[i])
				OPEN=open
			print("|OPEN|=",OPEN)
			
	Closed=CLOSED
	return State

#Driver Code
beta=2
bestNode=Bean_Search(Start,beta) #call search algorithm
print("Best Node=",bestNode)