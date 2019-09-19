import csv

def main():
	files = [
	'data/testmike_rightwrist_10-4_cd23_czyktrode-largepogo-velcro-strap_not_available_resting-not-holding-object_1-091819-1029.csv',
	'data/testmike_rightwrist_10-4_cd23_czyktrode-largepogo-velcro-strap_not_available_resting-not-holding-object_2-091819-1030.csv',
	'data/testmike_rightwrist_10-4_cd23_czyktrode-largepogo-velcro-strap_not_available_resting-not-holding-object_3-091819-1031.csv',
	'data/testmike_rightwrist_10-4_e638_czyktrode-largepogo-velcro-strap_not_available_resting-not-holding-object_1-091819-0710.csv',
	'data/testmike_rightwrist_10-4_e638_czyktrode-largepogo-velcro-strap_not_available_resting-not-holding-object_2-091819-0711.csv',
	'data/testmike_rightwrist_10-4_e638_czyktrode-largepogo-velcro-strap_not_available_resting-not-holding-object_3-091819-0712.csv',
	'data/testmike_rightwrist_10-4_f0ac_czyktrode-largepogo-velcro-strap_not_available_resting-not-holding-object_1-091819-0713.csv',
	'data/testmike_rightwrist_10-4_f0ac_czyktrode-largepogo-velcro-strap_not_available_resting-not-holding-object_2-091819-0714.csv',
	'data/testmike_rightwrist_10-4_f0ac_czyktrode-largepogo-velcro-strap_not_available_resting-not-holding-object_3-091819-0715.csv'
	]
	for file in files:
		times = []
		latencys = []
		#read in times from the current csv file
		with open(file, mode='r') as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line = 0
			#skips first row to avoid column descriptions
			for row in csv_reader:
				if line == 0:
					line += 1
				else:
					#adds a new time to the list
					times.append(float(row[0]))
					line += 1
			#stores all of the time differences
			latencys = calculateDeltaTime(times)

			#print out all relevant information for current file
			print('File Name/PATH: ', file)

			print('Min Latency: ', min(latencys))
			print('Max Latency: ', max(latencys))

			averageLatency = sum(latencys) / len(latencys)
			print('Average Latency: ', averageLatency)

def calculateDeltaTime(times):
	startTime = 0
	endTime = 0
	first = True
	latency = []
	#for each time, calculate difference
	for time in times:
		#if first value, the start and end are the same
			if first:
				startTime = time
				endTime = time
				#after this, will never be the first value
				first = False
			else:
				#uses the current iterations time as the end time, and the last iteration as the start time
				endTime = time
				latency.append(endTime - startTime)
				#set start time to current time for next iterations calculation
				startTime = time
	return latency	

if __name__ == "__main__":
	main()