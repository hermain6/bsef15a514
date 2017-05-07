count=0
j=0
n=1

time=[]
remainingtime=0
flag=0
timequantum=0
waitingtime=0
turnaroundtime=0
remain=0
arrivaltime=0
processes={}
bursttime=0
print ("enter total no of processes",n)

remain=n
for count in range (0,n):
	if(remainingtime[count]<=timequantum and remainingtime[count]>0):
		time+=remainingtime[count]
		remainingtime[count]=0
		flag =1
	else:
		if(remainingtime[count]>0):
			remainingtime[count]=timequantum
			time+=timequantum
	if(remainingtime[count]==0 and flag==1):
		remain=remain-1
		print (count+1,time-arrivaltime[count],time-arrivaltime[count]-bursttime[count])
		waitingtime+=time-arrivaltime[count]-bursttime[count]
		turnaroundtime+=time-arivaltime[count]
		flag=0
	if(count==n-1):
		count=0

	elif(arrivaltime[count+1]<=time):
		count=count+1
	else:
		count=0
print("average waiting time is",waitingtime/n)
print ("average turnaround time is",turnaroundtime/n)
