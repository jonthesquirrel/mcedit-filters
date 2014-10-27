# Copyright (c) 2014 Lasercar7 (@lasercar) - MIT License
# http://lasercar.github.io

#dictionary that maps block ids (to be collected) with readable names

#iterate through world, adding collected freq data to object/array
#def perform(level, box, options):
#	level.blockAt(x, y, x,)
data = [['elevation:', 1, 2, 3, 4, 5], ['Coal', 0, 1, 2, 3, 4], ['Iron', 2, 2, 2, 2, 2], ['Diamond', 4, 3, 2, 1, 0]]

#open csv file, write object to it
from os.path import expanduser
filepath = expanduser('~') + '/Downloads'

#iteration test
for column in range(len(data)):
	print ''
	for row in range(len(data[column])):
		print data[column][row]
