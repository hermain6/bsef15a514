n=1
bursttime=[]
arrivaltime=[]
waitingtime=[]
turnaroundtime=[]
averagewt=0
i=0
j=0
averagetat=0
n= input('Enter total no processes:')
for i in range(0,n):
	arr_time=input("arrival time:")
	arrivaltime.append(arr_time)
	b_time=input("burst time:")
	bursttime.append(b_time)
	

for i in range (0,n):
	waitingtime[i]=0
	for j in range (0,n):
		waitingtime[i]+=bursttime[i]
print (process,"\t", waitingtime,"\t" , bursttime, "\t" ,turnaroundtime)
for i in range (0,n):
	turnaroundtime[i]=waitingtime[i]+burstime[i]
	averagewt+=waitingtime
	averagetat+=turnaroundtime
	print ( i+1, bursttime[i], waitingtime[i],turnaroundtime[i])
averagewt/=i
averagetot/=i

print ("waiting time is:",averagewt)
print ("turn around time is:" ,averagetot)
