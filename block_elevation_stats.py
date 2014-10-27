# Copyright (c) 2014 Lasercar7 (@lasercar) - MIT License
# http://lasercar.github.io

#dictionary that maps block ids (to be collected) with readable names

stats = {}

#will be reference column in spreadsheet
stats['elevation:'] = map(lambda x: 0, range(256))

def logStat(block, elevation):
	if not block in stats:
	#initialize column
		stats[block] = map(lambda x: 0, range(256))

	#add to stat
	stats[block][elevation] += 1

#iterate through world and logStat()
#def perform(level, box, options):
#	level.blockAt(x, y, x)

#test
logStat('Diamond', 1)
logStat('Diamond', 1)
logStat('Diamond', 0)
print stats

#open csv file, write object (keys in reverse order) to it
#column = block, row = elevation + 1
from os.path import expanduser
filepath = expanduser('~') + '/Downloads'
