import time



import itertools 




w=[[0,172,145,607,329,72,312,120],
[172,0,192,494,209,158,216,92],
[145,192,0,490,237,75,205,100],
[607,494,490,0,286,545,296,489],
[329,209,237,286,0,421,49,208],
[72,158,75,545,421,0,249,75],
[312,216,205,296,49,249,0,194],
[120,92,100,489,208,75,194,0]]

dict1={0:"Brighton",1:"Bristol",2:"Cambridge",3:"Glasgow",4:"Liverpool",
       5:"London",6:"Manchester",7:"Oxford"}
 
def travel(w):
	
	n = len(w) 


	
	A = {(frozenset([0, i+1]), i+1): (costo, [0, i+1]) for i, costo in enumerate(w[0][1:])}


	for m in range(2, n):
		B = {}
		
		         
		for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, n), m)]:
			for j in S - {0}:
				 
				B[(S, j)] =min((A[(S-{j},k)][0] + w[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j) 
		A = B
	
		
	res = min([(A[d][0] + w[0][d[1]], A[d][1]) for d in iter(A)])
	

	Result1 = res[0]
	Result2=[dict1[i] for i in  res[1] ]
        
	l=[Result1,Result2]
	
	return l




