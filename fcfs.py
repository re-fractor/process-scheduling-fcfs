def calculate_time(atime,btime,ctime,ttime,wtime):
    etime = 0 #execution time for all 
    print("Process\tArrival time\tBurst time\tCompletion time\tTurnaround time\tWait time")
    for i in range(0,len(atime)):
        if atime[i]<=etime:   #check if arrival time is less/equal to total execution time done
            c = etime + btime[i]
            etime=c
        else:
            etime=atime[i]  #make execution time as arrival time of next process as CPU in idle state
            c=etime + btime[i]
            etime=c
        ctime.append(c)
        ttime.append(ctime[i]-atime[i])
        wtime.append(ttime[i]-btime[i])
        #print(etime)
        print(str(i+1) +"\t" + str(atime[i]) +"\t\t"+ str(btime[i]) +"\t\t"+ str(ctime[i]) +"\t\t"+ str(ttime[i]) +"\t\t"+ str(wtime[i]))

def avg_time(atime,ttime,wtime):
    st = 0
    sw = 0
    p = len(atime)
    for i in range(0,p):
        st+=ttime[i]
        sw+=wtime[i]
    print("Avg tat:",st/p)
    print("Avg wait time:",sw/p)
        
atime = [] #arrival time
btime = [] #burst time
ctime = [] #completion time
ttime = [] #turn around time
wtime = [] #wait time

num = int(input("No of processes?"))
for i in range(num):
    a = "Arrival time of p" + str(i+1) + ":"
    b = "Burst time of p" + str(i+1) + ":"
    atime.append(int(input(a)))
    btime.append(int(input(b)))


calculate_time(atime,btime,ctime,ttime,wtime)
avg_time(atime,ttime,wtime)