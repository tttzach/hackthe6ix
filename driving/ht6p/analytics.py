import pandas as pd
import numpy as np
from .range_speed import *

converted = []
timeInterval = 5
countSpeeds = 0
addSpeeds = 0

df = pd.read_csv("mynewtrip.csv", sep=';', usecols=['time','speed', 'area'])

def calculate():
	global converted
	global timeInterval
	global countSpeeds
	global addSpeeds
	for index, row in df.iterrows():
	    time = row['time']
	    speed = abs(row['speed'])
	    if timeInterval < time:
	        timeInterval += 5
	        newSpeed = int(addSpeeds * 3.6)
	        if newSpeed >= 5:
	            converted.append(newSpeed)
	        addSpeeds = 0
	    else:
	        addSpeeds += speed
	newSpeed = int(addSpeeds * 3.6)
	if newSpeed >= 5:
	    converted.append(newSpeed)

	converted.sort()

	firstq = np.percentile(converted, 25)
	secondq = np.percentile(converted, 50)
	thirdq = np.percentile(converted, 75)
	average = np.mean(converted)
	print(firstq, secondq, thirdq, average)
	return [firstq, thirdq]

hardbrakeCount = 0
consecutiveCount = 0
prevSpeed = None
prevTime = None
fast = False

def calculateBrake():
	for index, row in df.iterrows():
	    time = row['time']
	    speed = row['speed'] * 3.6
	    if not prevTime or prevTime + 0.2 <= time:
	        if not prevTime and speed > 32.1869:
	            prevSpeed = speed
	            prevTime = time
	            fast = True
	            continue
	        if fast:
	            if speed <= prevSpeed - 14.4841 or speed == 0:
	                prevSpeed = speed
	                prevTime = time
	                consecutiveCount += 1
	            else:
	                consecutiveCount = 0
	                prevSpeed = None
	                prevTime = None
	                fast = False
	                continue
	            if consecutiveCount == 3:
	                hardbrakeCount += 1
	                consecutiveCount = 0
	                prevSpeed = None
	                prevTime = None
	                fast = False
                

