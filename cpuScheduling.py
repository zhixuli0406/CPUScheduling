number = input("請輸入行程總數 : ")
lists = []
Arrival = []
Burst = []
for r in range(0,number):
        X = "p"+str(r)
        lists.append(X)
for r in range(0,number):
        AT = input("請輸入行程 "+lists[r]+" 到達的時間 : ")
        Arrival.append(AT)
for r in range(0,number):
        ET = input("請輸入行程 "+lists[r]+" 須執行的時間: ")
        Burst.append(ET)
ganttChart = []
clock = 0

copyOfListOfProcesses = list(lists)
copyOfArrivalTimes = list(Arrival)
copyOfBurstTimes = list(Burst)

copyOfListOfProcesses2 = list(lists)
copyOfArrivalTimes2 = list(Arrival)
copyOfBurstTimes2 = list(Burst)

print "行程總數 : ", number
print "行程列表 : ", lists
print "到達時間 : ", Arrival
print "執行時間 : ",Burst
print "\n"

######SRT######
print "\n"
print "######SRT(可搶先的SJF)######"
print "\n"

numberOfProcesses = number
listOfProcesses = list(lists)
ArrivalTimes = list(Arrival)
BurstTimes = list(Burst)

clock = 0

ganttChart = []

while numberOfProcesses != 0:
	temp = []
	for i in range(len(ArrivalTimes)):
		if ArrivalTimes[i] <= clock :
			temp.append(BurstTimes[i])
	if temp :
		minimumExecutionTime = min(temp)
		for j in range(len(BurstTimes)):
			if BurstTimes[j] == minimumExecutionTime:
				tmp = j
				ganttChart.append(listOfProcesses[j])
				BurstTimes[j] -= 1
				if BurstTimes[j] == 0:
					listOfProcesses.remove(listOfProcesses[j])
					ArrivalTimes.remove(ArrivalTimes[j])
					BurstTimes.remove(BurstTimes[j])	
					numberOfProcesses = numberOfProcesses - 1
				break
		clock +=1
	else :
		clock += 1
		ganttChart.append("X")

print "ganttChart: ", ganttChart

WT = []
CT = []
TAT = []
for i in range(len(copyOfListOfProcesses)):
	WT.append(0)
	CT.append(0)
	TAT.append(0)
for i in range(len(ganttChart)-1,0,-1):
	if ganttChart[i] != "X":
		Q = int(ganttChart[i][1:])
		if CT[Q] == 0:
			CT[Q] = i+1
for i in range(len(copyOfListOfProcesses)):
	TAT[i] = CT[i] - copyOfArrivalTimes[i]
for i in range(len(copyOfListOfProcesses)):
	WT[i] = TAT[i] - copyOfBurstTimes[i]
WaitingsTime = float(sum(WT))/len(copyOfListOfProcesses)
print "waiting time: ", WaitingsTime

TurnAroundTime = float(sum(TAT))/len(copyOfArrivalTimes)

print "turnAround time: ", TurnAroundTime

######SJF######
print "\n"
print "######SJF(不可搶先的SJF)######"
print "\n"

numberOfProcesses = number
listOfProcesses = list(lists)
ArrivalTimes = list(Arrival)
BurstTimes = list(Burst)

clock = 0

ganttChart = []

while numberOfProcesses != 0:
	
	temp = []
	for i in range(len(ArrivalTimes)):
		if ArrivalTimes[i] <= clock :
			temp.append(BurstTimes[i])
	if temp:
		minimumExecutionTime = min(temp)
		for j in range(len(BurstTimes)):
			if BurstTimes[j] == minimumExecutionTime:
				tmp = j
				for p in range(BurstTimes[j]):
					ganttChart.append(listOfProcesses[j])
				listOfProcesses.remove(listOfProcesses[j])
				ArrivalTimes.remove(ArrivalTimes[j])		
		clock = clock + BurstTimes[tmp]
		BurstTimes.remove(BurstTimes[tmp])
		numberOfProcesses = numberOfProcesses - 1
	else :
		clock += 1
		ganttChart.append("X")

print "ganttChart: ", ganttChart

		

WT = []
for i in range(len(copyOfListOfProcesses)):
	WT.append(ganttChart.index("p" + str(i)))

WaitingsTime = float(sum(WT))/len(copyOfListOfProcesses)

print "waiting time: ", WaitingsTime

turnAroundTimes = []

for i in range(len(copyOfArrivalTimes)):
	turnAroundTimes.append((len(ganttChart) - ganttChart[::-1].index("p" + str(i)) - 1) - copyOfArrivalTimes[i])

TurnAroundTime = float(sum(turnAroundTimes))/len(copyOfArrivalTimes)

print "turnAround time: ", TurnAroundTime


####FCSF####
print "\n"
print "######FCSF######"
print "\n"

numberOfProcesses = number
listOfProcesses = list(lists)
ArrivalTimes = list(Arrival)
BurstTimes = list(Burst)

clock = 0

ganttChart = []

while len(listOfProcesses) != 0:
	lenghtOfArrivalTimes = len(ArrivalTimes) 

	temp = []
	temp2 = []
	for i in range(lenghtOfArrivalTimes):
		if ArrivalTimes[i] <= clock:
			temp.append(ArrivalTimes[i])
	if temp :
		minimumArrivalTime = min(temp)
		for j in range(lenghtOfArrivalTimes):
			if ArrivalTimes[j] == minimumArrivalTime:
				for p in range(BurstTimes[j]):
					ganttChart.append(listOfProcesses[j])
				clock = clock + BurstTimes[j]
				temp2.append(j)		
		for i in sorted(temp2, reverse = True):
			del BurstTimes[i]
			del ArrivalTimes[i]
			del listOfProcesses[i]
		numberOfProcesses = numberOfProcesses - 1
	else :
		clock += 1
		ganttChart.append("X")
print "ganttChart: ", ganttChart


WT = []
for i in range(len(copyOfListOfProcesses)):
	WT.append(ganttChart.index("p" + str(i)))

WaitingsTime = float(sum(WT))/len(copyOfListOfProcesses)

print "waiting time: ", WaitingsTime

turnAroundTimes = []

for i in range(len(copyOfArrivalTimes)):
	turnAroundTimes.append((len(ganttChart) - ganttChart[::-1].index("p" + str(i)) - 1) - copyOfArrivalTimes[i])

TurnAroundTime = float(sum(turnAroundTimes))/len(copyOfArrivalTimes)

print "turnAround time: ", TurnAroundTime
			
####RR####

print "\n"
print "######RR######"
print "\n"

numberOfProcesses = number
listOfProcesses = list(lists)
ArrivalTimes = list(Arrival)
BurstTimes = list(Burst)

clock = 0

ganttChart = []

quantom = input("請輸入行程分割數: ")


AE = zip(ArrivalTimes,BurstTimes)
AE.sort()

ArrivalTimes_sorted = [ArrivalTimes for ArrivalTimes, BurstTimes in AE]

BurstTimes_sorted = [BurstTimes for ArrivalTimes, BurstTimes in AE]



Al = zip(copyOfArrivalTimes,listOfProcesses)
Al.sort()
listOfProcesses_sorted = [listOfProcesses for copyOfArrivalTimes, listOfProcesses in Al]


while len(listOfProcesses_sorted) != 0:

	flag = False

	
	for i in range(len(AE)):
		
		for j in range(quantom):
			if BurstTimes_sorted[i] > 0:

				BurstTimes_sorted[i] = BurstTimes_sorted[i] - 1
				ganttChart.append(listOfProcesses_sorted[i])

			else:
				newTmp = i
				flag = True
				break

	if flag == True:
		del BurstTimes_sorted[newTmp]
		del AE[newTmp]
		del listOfProcesses_sorted[newTmp]
		del ArrivalTimes_sorted[newTmp]

print "ganttChart: ", ganttChart

WT = []
for i in range(len(copyOfListOfProcesses2)):
	WT.append(turnAroundTimes[i] - copyOfBurstTimes[i])

WaitingsTime = float(sum(WT))/len(copyOfArrivalTimes2)

print "waiting time: ", WaitingsTime

turnAroundTimes = []

for i in range(len(copyOfArrivalTimes2)):
	turnAroundTimes.append((len(ganttChart) - ganttChart[::-1].index("p" + str(i)) - 1) - copyOfArrivalTimes2[i])

TurnAroundTime = float(sum(turnAroundTimes))/len(copyOfArrivalTimes2)

print "turnAround time: ", TurnAroundTime

