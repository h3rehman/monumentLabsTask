import time
import shlex
from subprocess import *


'''
Popen Solution (non threaded), using an active loop (while loop) to time the tasks
'''

#This solution is not workable with find commands i.e. 'find /' or 'find /usr'
commands = ['sleep 3', 'ls -l /', 'find /', 'sleep 4', 'find /usr', 'date', 'sleep 5', 'uptime']

#Works with these commands though
#commands = ['sleep 3', 'ls -l /','sleep 4','date', 'sleep 5']

exec_time = {}
running = {}

for command in commands:

    cmd = shlex.split(command)
    exec_time[command] = time.time()
    #starting each process one by one and its time above. 
    running[command] = Popen(cmd, stdout=PIPE, stderr=PIPE)


while len(running):

    executed = set()

    for command, proc in running.items():
        if proc.poll() is not None:
            exec_time[command] = round(time.time() - exec_time[command], 3)
            executed.add(command)
     

    #removing any commands that have been finished
    for command in executed:
        del running[command]

#printing out execution times        
print (exec_time)
