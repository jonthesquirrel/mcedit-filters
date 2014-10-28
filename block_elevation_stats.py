# Copyright (c) 2014 Lasercar7 (@lasercar) - MIT License
# http://lasercar.github.io

#TODO: dictionary that maps block ids (to be collected) with readable names

stats = {}
def logStat(block, elevation):
	if not block in stats:
	#initialize column
		stats[block] = map(lambda x: 0.0, range(256))

	#add to stat
	stats[block][elevation] += 1

#MCEdit user options
inputs = (
	('Scan Radius', 100)
)

#test
logStat('Coal', 3)
logStat('Diamond', 1)
logStat('Diamond', 1)
logStat('Gold', 1)
logStat('Diamond', 0)

#init
def perform(level, box, options):

	#iterate through world and logStat(block, y)

	level.blockAt(x, y, x)


#calculate total blocks from scan radius, then convert raw data to percentage
options = {'Scan Radius': 100}#temp
layerTotal = (float(options['Scan Radius']) * 2) **2
def percentFormat():
	for block in stats:
		i = 0
		for elevation in stats[block]:
			stats[block][i] = float(elevation)/layerTotal
			i += 1

percentFormat()

#open csv file, convert stats to data, write data to file
from os.path import expanduser, exists
def filename():
	prefix = expanduser('~') + '/Downloads/BlockElevationStats'
	postfix = '.csv'
	path = prefix + postfix
	i = 1
	while exists(path):
		i += 1
		path = prefix + str(i) + postfix
	return path

import csv
with open(filename(), 'wb') as csvFile:
	writer = csv.writer(csvFile, dialect='excel')

	#de-objectify data
	data = []
	for key, value in stats.iteritems(): # stats.items() in python 3.x
		data.append([key] + value)

	#translate column structure to row structure
	grid = map(list, zip(*data))

	#write to file
	i = -1
	for row in grid:
		if i == -1:
			writer.writerow(['elevation:'] + row)
		else:
			writer.writerow([i] + row)
		i += 1

#TODO: move all stuff, including functions, into perform()
