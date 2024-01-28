import random,sys,math

SuccList ={ 'A':[['T',11],['B',13],['C',21]],
			'T':[['D',27],['B',13]],
			'B':[['D',27],['E',3]],
			'C':[['F',25],['G',4]],
			'D':[['H',101],['I',99]],
			'F':[['J',67]],
			'G':[['K',99],['L',3]],
			'H':[['M',17]],
			'I':[['M',17]],
			'J':[['M',17]]
			}
Start='A'

Closed = list()
def MOVEGEN(N):
	New_list=list()
	if N in SuccList.keys():
		New_list=SuccList[N]
	
	return New_list

def heu(Node): #Node = ['B',2]--> [Node[0],Node[1]]
	return Node[1]

def APPEND(L1,L2):
	New_list=list(L1)+list(L2)
	return New_list

def exp_schedule(k=20, lam=0.005, limit=100):

    return lambda t: (k * math.exp(-lam * t) if t < limit else 0)

def Simulated_Annealing(schedule=exp_schedule()):
	global Closed
	node=[Start,5]
	bestNode=node
	CLOSED=[node]
	
	print("\nInitial Point=",node)
	for t in range(sys.maxsize):
		print("\n*******************************")
		print("For iteration i=",t)
		T=schedule(t)
		if T == 0:
			return bestNode
		
		CHILD = MOVEGEN(node[0])
		if(len(CHILD) == 0):
			return bestNode
		
		node=random.choice(CHILD)
		CLOSED=APPEND(CLOSED,[node])
		print("\nCurrent node=",node)
		print("Closed List=",CLOSED)
		delta_e = heu(node) - heu(bestNode)

		if delta_e >0 and 1/(1+(math.exp(delta_e / T)))>random.choice([0,1]) :
			bestNode=node
			
	Closed=CLOSED
	return bestNode
	
#Driver Code
bestNode=Simulated_Annealing() #call search algorithm
print("Best Node=",bestNode)