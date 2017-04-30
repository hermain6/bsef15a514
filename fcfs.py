process_queue=[ ]
total=0
total_waitingtime=0
n= int(raw_input('Enter total no processes:'))
for i in range(0,n):
	process_queue.append([])
	process_queue[i].append(raw_input('Enter process name:'))
	process_queue[i].append(int(raw_input('Enter process arrival time:')))
	total_waitingtime+=process_queue[i][1]
	process_queue[i].append(int(raw_input('Enter process burst time: ')))
	print " "
	process_queue.sort(key=lambda process_queue:process_queue[1])
	 
for i in range(0,n):
	print process_queue[i][0],'\t\t',process_queue[i][1],'\t\t', process_queue[i][2]
	min=total
	if(total>0):
  		print '0 ----------',total
	for i in range(1,n+1):
		print min, "_____________" ,total
		min=total

print "average waiting time",(total_waitingtime/n) 