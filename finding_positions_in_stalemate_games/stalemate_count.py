n = 9
f = open('step_'+str(n)+'_non_complete_games.txt','r')
lines = f.readlines()
f.close()

f1 = open('observations.txt','w')

count_values = [0,0,0,0,0,0,0,0,0]
for line in lines:
	temp = line.strip().split(',')
	for i in range(0,9):
		if line[i] == '1':
				count_values[i] = count_values[i]+1
f1.write('this is for stale mate positions'+str(count_values)+'\n')
f1.close()
