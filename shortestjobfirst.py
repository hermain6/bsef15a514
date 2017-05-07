process={}
wt=[]
bt=[]
tat=[]
total=0
temp=0
i=0
at=[]
j=0
n=1
pos=0
avgwt=1.0
avgtat=1.0

n= input("total no of processes")
for i in range (0,n):
	arr_time=input("arrival time:")
	at.append(arr_time)
	b_time=input("burst time:")
	bt.append(b_time)
for i in range (0,n):
	pos=i
	for j in range (0,n):
		if(bt[j]<bt[pos]):
			pos=j
	temp=bt[i]
	bt[i]=pos[i]
	bt[pos]=temp
	
	temp=process[i]
	process[i]=process[pos]
	process[pos]=temp
for i in range (0,n):
	wt[i]=0
	for j in range (0,n):
		wt[i]+=bt[j]
	total+=wt[i]
avgwt= total*1.0/n
total =0
print (process, "\t", wt , "\t" ,bt ,"\t" ,tat)
for i in range (0,n):
	tat[i]=bt[i]+wt[i]
	total+=tat[i]
	print (process, "\t", wt , "\t" ,bt ,"\t" ,tat)
avgtat=toal*1.0/n
print ("average waiting time is :" ,avgwt)
print ("average turn around time is:", avgtat)
