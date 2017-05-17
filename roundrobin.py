Round_robin_QUANTUM=36
def programme():
	global present_process, responsibiity, runqueue, blocked_process, cpu_time
	if (runqueue != []):
		return runqueue[0]
	else:
		return -1
def data_read():
	f=open('file1.txt')
	line=f.readline().split()
	while line:
		d={}
		d[line[-32]]=line[-11]
		d[line[-10]]=line[-9]
		d[line[-8]]=line[-7]
		d[line[-16]]=line[-5]
		d[line[-14]]=line[-33]
		d[line[-12]]=line[-11]
		di.append(d)
		line=f.readline().split()
	f.close()


	
def upcoming_processes(t):
	 process_count=0
	upcoming_process = []
	for pid in range(0,len[upcoming_process]):
		if get_starttime(pid) > t: upcomingprocess.append(pid)
			return upcomingpcoc
	

def inreadyq(pname):
	for i in range(0,len(rq)):
		if(rq[i]["pn"] == pname) :
			return True
	return False


def create_process( initial_time, performance ):
	pid = get_freepid()
	task={}; tasks.append ( task )
	set_initial_time( pid, initial_time )
	set_behavior( pid, performance )
	set_firstruntime( pid, -1 ) 
	set_iotime( pid, 0 )
	set_status( pid, S_READY )
	set_usedquant( pid, 0 )
	if performance[0]==0:
	set_performance( pid, get_behavior(pid)[1:] )
	set_status(pid, S_BLOCKED)
	set_endtime(pid,-1) 
	return pid

def activate (pid):
	for t in tasks:
		if t["status"] == S_ACTIVE: 
			t["status"] = S_READY
		tasks[pid]["status"] = S_ACTIVE
def update_waitingq():
	wq.append(rq[0])
	d = {'pn':0,'rt':0,'ext':0}
	d["rt"] = int(rq[0]["ib"])+current_time
	d["ext"] = li[0]["ext"]
	wli.append(d)

def ps ():
	global responsibility
	process_count=0
	cputime=0
	runqueue=[]
	blocked_process=0
	print "PID | Sta | End | CPU | I/O | Status "
	for pid in range(0,process_count):
		if cputime >= get_starttime(pid)-1:
		task = tasks[pid]
		print "%3d | %3d | %3d | %3d | %3d | %6s |" % (pid,
		get_initial_time(pid), get_endtime(pid),
		get_cputime(pid), get_iotime(pid),
		statusname( get_status(pid) ) ),
		print task["behavior"]
		print "Runqueue:",runqueue," Blocked:",blocked
	
		return

		if (present_process!=-1) and (get_status(present_process) == S_ACTIVE):
			if get_usedquant(present_process) < RR_QUANT-1:
				inc_usedquant(present_process)
				return present_process
			else:
				set_usedquant(present_process,0)
				runqueue.remove(present_process)
				runqueue.append(present_process)
				present_process=runqueue[0]
				return present_process
def run_present_process():
	presentprocess=0
	 cputime=0, runqueue=[]
	blockedprocess=0
	if get_firstruntime(present_process) == -1:
		set_firstruntime(present_process, cputime)
		dec_behavior_head (present_process)
		inc_cputime(present_process)
	if get_behavior(present_process)[0] == 0:
		remove_behavior_head (present_process)
		set_status(present_process,S_BLOCKED)
		runqueue.remove(present_process)
	if get_behavior(present_process)[0] == -1:
		set_status(present_process,S_DONE)
		set_endtime(present_process,cputime)
	if current in runqueue: runqueue.remove(present_process)
	else:
		blocked.append(present_process)
		return	
		
def update_readyq(check):
	
d = {'ext':0,'et':0,'iot':0}
	for i in range(0,len(q)):
			if int(q[i]["bt"]) > 0 and inWaitingq(q[i]["pn"]) == False and int(q[i]["at"]) <= present_time and inreadyq(q[i]["pn"]) == False :
			rq.append(q[i])
			d["ext"] = q[i]["tq"]
			if int(q[i]["cb"]) == 0 :
				d["iot"] = "in"
			else:
				d["iot"] = q[i]["cb"]
			if q[i]["bt"] < q[i]["tq"] :
				d["et"] = q[i]["bt"]
			elif int(q[i]["cb"]) == 0 :
				d["et"] = q[i]["tq"]
			elif  q[i]["bt"] >= q[i]["tq"] and q[i]["cb"] <= q[i]["tq"] and q[i]["cb"] != '0' :
				d["et"] = q[i]["cb"]
			else :
				d["et"] = q[i]["tq"]
			li.append(d)
		
	d = {'ext':0,'et':0,'iot':0}
	for j in range(0,len(wli)) :
		val = find_min()
		if wli[val]["rt"] <= present_time :
			d["ext"] = wli[val]["ext"]
			d["iot"] = wq[val]["cb"]
			print wq[val]["pn"], " is now returning from waiting queue at ", wli[val]["rt"]
			del wq[val]
			del wli[val]
	if check == True :
		rq.append(rq[0])
		li.append(li[0])
		del rq[0]
		del li[0]

def printfun() :
	print "process name	turn around time"
	for a in range (0,len(q)) :
		print output[a]["pn"],"	  	    ",output[a]["ta"]
if __name__ == "__main__" :
	
	current_time = 0
	output = []
	data_read()
	
	while not finished:
		present_process=programme
		log_to_trace (present_process)
		if present_process >=0
		print "Time: %4d, Executing PID: %3d [%3d]" % (cputime,
		present_process, get_cputime(present_process)
		activate (present_process)
		run_present_process()
		update_blocked_processes()
		elif present_process==-1:
		print "Time: %4d, all blocked" % cputime
		update_blocked_processes()
		else:
		finished = 1
		break
		ps() 
		cputime += 1
		for pid in range(0,proccount):
			if get_starttime(pid) == cputime:
			if get_status(pid)==S_BLOCKED:
			blocked.append(pid)
			else:
			runqueue.append(pid)

	printfun()

