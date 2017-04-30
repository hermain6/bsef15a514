total=0
processes={}
burst_time=[]
arrival_time=[]
remaining_time=[]
processtime=[]
processgantt=[100]
smallest=0
sum_wait=0
sum_turnaround=0
endtime=[]
i=0
time=[]
remain=0
n=input("enter total number of processes:")
for i in range(0,n):
	a_time=input("arrival time:")
	arrival_time.append(a_time)
	b_time=input("burst time:")
	burst_time.append(b_time)
	
for i in range(0,n):
	print arrival_time[0],"\t",burst_time[i]
burst_time.sort()

remaining_time.sort()

min=total
if(total>0):
	remain=remain+1
	endtime=time+1
	print(smallest+1,endtime-arrival_time[smallest],endtime-burst_time[smallest]-arrival_time[smallest])
	sum_wait+=endtime-burst_time[smallest]-arrival_time[smallest]
	sum_turnaround+=endtime-arrival_time[smallest]
print("average waiting time is:" ,sum_wait*1.0/n)
print("average turn arount time is:"),sum_turnaround*1.0/5
for i in range(0,n):
	print(i,total+1)