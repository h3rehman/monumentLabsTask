import subprocess
import shlex
import time
import threading

'''
Using subprocess.call() function to run processes and timing each process. 
Finally giving the output of Max, min and Average time taken by each processes. 
'''

commands = ['sleep 3', 'ls -l /', 'find /','sleep 4','find /usr','date', 'sleep 5','uptime']
    

exec_time = {}

def time_it(command):
    start_time = time.time()
    cmd = shlex.split(command)
    subprocess.call(cmd)
    exec_time[command] = time.time() - start_time

threads = []

for command in commands:
    t = threading.Thread(target=time_it,args=(command,))
    t.start()
    threads.append(t)


for t in threads:
    t.join()

print('\n')
print('Commands ', '|', '  Execution Time', '\n')

sum = 0
maxT = 0
minT = 10

for k in sorted(exec_time, key=exec_time.get, reverse=True):
    print('{} {} {} {}'.format(k,' | ', round(exec_time[k], 3), ' secs'))
    sum += round(exec_time[k])
    #max time
    if exec_time[k] > maxT:
        maxT = round(exec_time[k], 3)
    #min time
    if exec_time[k] < minT:
        minT = round(exec_time[k], 3)
    
#Average Time    
avgT = round(sum/len(exec_time), 3)

print()
print('Max, min and Average times are: \n')
print ('Max Time: ',maxT, 'secs')
print ('Min Time: ',minT, 'secs')
print('Average Time: ', avgT, 'secs \n')
