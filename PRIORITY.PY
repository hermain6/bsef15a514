process={}
priority=[]
key=1
loc=1
bursttime=[]
arrivaltime=[]
temp=0
max=0
wt=0
ta=0
sum=0
i=0
j=0

n=input("enter no of processes:")
for i in range(0,n):
	prio_no=input("priority number:")
	priority.append(prio_no)
	a_time=input("arrival time:")
	arrivaltime.append(a_time)
	b_time=input("burst time:")
	bursttime.append(b_time)
for i in range (0,n):
	max=i
	for j in range (0,n):
		if(priority[j] < priority[max]):
			priority[max]=priority[i]
			priority[i]=temp
			temp=bursttime[i]
			bursttime[max]=bursttime[i]
			bursttime[i]=temp
			temp=process[max]
			process[max]=process[i]
			process[i]=temp
for i in range (0,n):
	wt[i+1]=bursttime[i]+wt[i]
	ta[i]=bursttime[i]+wt[i]
	sum+=ta[i]

for i in range (0,n):
	print ("waiting time is:" , process[i], wt[i])
	print ( "turn around time is:" , process[i], ta[i])
print ("average turn around time is:" ,sum/n)
