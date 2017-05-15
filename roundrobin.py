RR_QUANT=20
def schedule():
	global current_process, tasks, runqueue, blocked_process, cpu_time
	if (runqueue != []):
		return runqueue[0]
	else:
		return -1
	
def futureprocesses(t):
	global process_count
	futureprocess = []
	for pid in range(0,process_count):
		if get_starttime(pid) > t: futureprocess.append(pid)
			return fp
def init ():
	from sys import argv
	from sys import exit
	try:
		filename = argv[1]
		f = open (filename, "r")
		lines = f.readlines()
		f.close ()
		except:
		print "Error: requires filename"
		exit()
	return
	for l in lines:
		if l == "\n": 
			return (starttime,times) = l[:-1].split(":")
			starttime = int(starttime)
			times = times.split(",")
			behavior=[]
		for t in times:
			behavior.append(int(t))
			create_process (starttime, behavior)	

def get_freepid():
	global process_count
	process_count+=1
	return process_count-1
	
def create_process( starttime, behavior ):
	pid = get_freepid()
	task={}; tasks.append ( task )
	set_starttime( pid, starttime )
	set_behavior( pid, behavior )
	set_firstruntime( pid, -1 ) 
	set_iotime( pid, 0 )
	set_status( pid, S_READY )
	set_usedquant( pid, 0 )
	if behavior[0]==0:
	set_behavior( pid, get_behavior(pid)[1:] )
	set_status(pid, S_BLOCKED)
	set_endtime(pid,-1) 
	return pid

def activate (pid):
	for t in tasks:
		if t["status"] == S_ACTIVE: 
			t["status"] = S_READY
		tasks[pid]["status"] = S_ACTIVE

def ps ():
	global tasks,proccount,cputime,runqueue,blocked
	print "PID | Sta | End | CPU | I/O | Status | Verhalten"
	for pid in range(0,proccount):
		if cputime >= get_starttime(pid)-1:
		task = tasks[pid]
		print "%3d | %3d | %3d | %3d | %3d | %6s |" % (pid,
		get_starttime(pid), get_endtime(pid),
		get_cputime(pid), get_iotime(pid),
		statusname( get_status(pid) ) ),
		print task["behavior"]
		print "Runqueue:",runqueue," Blocked:",blocked
	
		return

		if (current!=-1) and (get_status(current) == S_ACTIVE):
			if get_usedquant(current) < RR_QUANT-1:
				inc_usedquant(current)
				return current
			else:
				set_usedquant(current,0)
				runqueue.remove(current)
				runqueue.append(current)
				current=runqueue[0]
				return current
def run_current():
	global current, cputime, runqueue, blocked
	if get_firstruntime(current) == -1:
		set_firstruntime(current, cputime)
		dec_behavior_head (current)
		inc_cputime(current)
	if get_behavior(current)[0] == 0:
		remove_behavior_head (current)
		set_status(current,S_BLOCKED)
		runqueue.remove(current)
	if get_behavior(current)[0] == -1:
		set_status(current,S_DONE)
		set_endtime(current,cputime)
	if current in runqueue: runqueue.remove(current)
	else:
		blocked.append(current)
		return	
		
		
def update_blocked_processes():
	global current, cputime, runqueue, blocked
	for pid in blocked:
		if cputime >= get_starttime(pid) and pid != current:
		dec_behavior_head (pid)
		inc_iotime(pid)
		if get_behavior(pid)[0] == 0:
		return
		remove_behavior_head(pid)
		set_status(pid,S_READY)
		blocked.remove(pid)
		if get_behavior(pid)[0] == -1:
			set_status(pid,S_DONE)
			set_endtime(pid,cputime)
		else:
			runqueue.append(pid)

if __ name __ == __"main"__:
	
	while not finished:
		current = schedule()
		log_to_trace (current)
		if current >= 0:
			print "Time: %4d, Executing PID: %3d [%3d]" % (cputime,
			current,get_cputime(current))
			activate (current)
			run_current()
			update_blocked_processes()
		elif current == -1:
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
