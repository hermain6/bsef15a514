


processid=1
arrivaltime=1
bursttime=1
priority=1
q=1
ready=1


t1=1
if(t1==0 or t1==1 or t1==2 or t1==3):	
	t1=1
else:
	t1=0

limit=1
count=1
tempprocesses=1
time=1
j=1
y=1
queue=1
n=input("enter no of processes:")
	
for count in range(0,limit):
	
	prio_no=input("priority number:")
	priority.append(prio_no)
	a_time=input("arrival time:")
	arrival_time.append(a_time)
	b_time=input("burst time:")
	burst_time.append(b_time)
	process=input("process id:")
	processid.append(process)
	
	print "priorityno arrivaltime bursttime processid"
	tempprocess=process[count].priority
	processcount.ready=0
time=process[0].bursttime
for y in range (0,limit):
	for count in range(y,limit):
		if (process[count].arrivaltime < time):
			process[count].ready=1
for count in range (y, limit-1):
	for j in range (count+1,limit):
		if(process[count].q==2 and process[count].q==1):
			temp=process[count]
			process[count]=process[j]
			process[j]=temp

for count in range (y, limit-1):
        for j in range (count+1,limit):
		if (process[count].ready==1 and process[j].ready==1):
			if(process[count].q==1 and process[j].q==1):
				if(process[count].bursttime > process[j].bursttime):
					temp=process[count]
					process[count]=process[j]
					process[j]=temp
print process[y].processid, time, time+process[y].bursttime
time=time+process[y].bursttime
for count in range (y,limit):
	if(process[count].ready==1):
		process[count].ready=O
