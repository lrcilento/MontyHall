import numpy

def run():

	totalDoors = 3
	totalIterations = 10000

	doors = []
	switchVictories = 0
	stickVictories = 0

	for i in range (totalDoors):
		doors.append(i + 1)

	for i in range (totalIterations):
		victory = numpy.random.choice(doors)
		choice = numpy.random.choice(doors)
		if choice == victory:
			stickVictories += 1
		else:
			switchVictories += 1

	switchVictoriesProbability = (switchVictories/totalIterations)*100
	stickVictoriesProbability = (stickVictories/totalIterations)*100

	print(f'Doors: {totalDoors} | Iterations: {totalIterations}\n')
	print(f'Win% Switching Doors: {switchVictoriesProbability}%')
	print(f'Win% Without Switching: {stickVictoriesProbability}%\n')