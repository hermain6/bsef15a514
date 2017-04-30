#!usr/bin/env python
total =0
processes={ }
arrival_time=[]
burst_time=[]
n=input("enter total processes:")
for i in range(0,n):
	arr_time=input("arrival time:")
	arrival_time.append(arr_time)
	b_time=input("burst time:")
	burst_time.append(b_time)
	processes[burst_time[i]]=[i+1,arrival_time[i]]
	print "arrival time\t burst time"
for i in range(0,n):
	print ("arrival_time[0] 	 burst_time[i]")
	burst_time.sort()
	total=processes.get(burst_time[0])[1]
	min=total
	if(total>0):
		print "0 ______",total
for i in range(0,n):
	total=total+burst_time[i]

	print min,"_______",total
	min=total