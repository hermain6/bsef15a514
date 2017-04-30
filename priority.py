#!user/bin/env python
total=0
priority=[]
processes={}
burst_time=[]
arrival_time=[]
n=input("enter no of processes:")
for i in range(0,n):
	prio_no=input("priority number:")
	priority.append(prio_no)
	a_time=input("arrival time:")
	arrival_time.append(a_time)
	b_time=input("burst time:")
	burst_time.append(b_time)
	processes[priority[i]]=[i+1,arrival_time[i],burst_time[i]]
	print "priorityno arrivaltime bursttime"
for i in range(0,n):
	print priority[i], "\t" , arrival_time[i], "\t" ,burst_time[i]
	priority.sort()
	total=processes.get(priority[0])[1]
	min=total
	if(total>0):
		print"0 __________",total
for i in range(0,n):
	total=total+1
processes.get(priority[i])[2]
print min,"__________",total
min=total